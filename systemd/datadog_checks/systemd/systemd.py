# (C) Datadog, Inc. 2019
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import copy
from collections import defaultdict
import pystemd
from pystemd.systemd1 import Manager
from pystemd.systemd1 import Unit

from datetime import datetime

from datadog_checks.base import AgentCheck, ConfigurationError, is_affirmative


class SystemdCheck(AgentCheck):

    UNIT_STATUS_SC = 'systemd.unit.active'

    def __init__(self, name, init_config, agentConfig, instances=None):
        if instances is not None and len(instances) > 1:
            raise ConfigurationError('Systemd check only supports one configured instance.')
        super(SystemdCheck, self).__init__(name, init_config, agentConfig, instances)

        instance = instances[0]
        self.collect_all = is_affirmative(instance.get('collect_all_units', False))
        self.units = instance.get('units', [])
        # to store the state of a unit and compare it at the next run
        self.unit_cache = defaultdict(dict)

        # unit_cache = {
        #    "units": {
        #        "<unit_name>": "<unit_status>",
        #        "cron.service": "inactive",
        #        "ssh.service": "active"
        #    },
        #    "change_since": "iso_time"
        #}
      
    def check(self, instance):
        
        if self.units:
            # self.log.info(units)
            for unit in self.units:
                self.get_unit_state(unit)
        if self.collect_all == True:
            # we display status for all units if no unit has been specified in the configuration file
            self.get_active_inactive_units()

        self.log.info("unit_cache is... ")
        self.log.info(self.unit_cache)
        
        self.get_all_units(self.units)

    def get_all_units(self, instance):
        cached_units = self.unit_cache.get('units')
        changes_since = datetime.utcnow().isoformat()
        if cached_units is None:
            updated_units = self.get_listed_units()
        else:
            previous_changes_since = self.unit_cache.get('units', {}).get('changes_since')
            updated_units = self.update_unit_cache(cached_units, previous_changes_since)
            self.log.info(previous_changes_since)

        # Initialize or update cache for this instance
        self.unit_cache = {
            'units': updated_units,
            'changes_since': changes_since
        }

        self.log.info(self.unit_cache)
    
    def get_listed_units(self):
        manager = Manager()
        manager.load()

        units = self.units

        mytemp_dict = {}

        mytemp_dict = {unit: self.get_state_single_unit(unit) for unit in units}

        self.log.info(mytemp_dict)

        return mytemp_dict

    def update_unit_cache(self, cached_units, changes_since):
        units = copy.deepcopy(cached_units)

        updated_units = self.get_listed_units()

        self.log.info(units)

        returned_cache = {}

        returned_cache = updated_units
        # returned_cache['changes_since'] = changes_since

        self.log.info(returned_cache)

        return returned_cache  # a new cache, dict of units and timestamp

    def get_active_inactive_units(self):
        # returns the number of active and inactive units
        manager = Manager()
        manager.load()
        list_units = manager.Manager.ListUnitFiles()

        # remove units that have an @ symbol in their names - cannot seem to get unit info then - to investigate
        unit_names = [unit[0] for unit in list_units if '@' not in unit[0]]

        active_units = inactive_units = 0

        for unit in unit_names:
        # full unit name includes path e.g. /lib/systemd/system/networking.service - we take the string before the last "/"
            unit_short_name = unit.rpartition('/')[2]
            # self.log.info(unit_short_name)
            try:   
                unit_loaded = Unit(unit_short_name, _autoload=True)
                unit_state = unit_loaded.Unit.ActiveState
                if unit_state == b'active':
                    active_units += 1
                if unit_state == b'inactive':
                    inactive_units += 1
            except pystemd.dbusexc.DBusInvalidArgsError as e:
                self.log.debug("Cannot retrieve unit status for {}".format(unit_short_name))
        
        self.gauge('systemd.units.active', active_units)
        self.gauge('systemd.units.inactive', inactive_units)

    def get_state_single_unit(self, unit_id):
        try:
            unit = Unit(unit_id, _autoload=True)
            # self.log.info(str(unit_name))
            state = unit.Unit.ActiveState
            return state
        except pystemd.dbusexc.DBusInvalidArgsError as e:
            self.log.info("Unit name invalid for {}".format(unit_id))
        
    def get_unit_state(self, unit_id):
        try:
            unit = Unit(unit_id, _autoload=True)
            # self.log.info(str(unit_name))
            state = unit.Unit.ActiveState
            # Send a service check: OK if the unit is active, CRITICAL if inactive
            if state == b'active':
                self.service_check(
                    self.UNIT_STATUS_SC,
                    AgentCheck.OK,
                    tags=["unit:{}".format(unit_id)]
                )
            elif state == b'inactive':
                self.service_check(
                    self.UNIT_STATUS_SC,
                    AgentCheck.CRITICAL,
                    tags=["unit:{}".format(unit_id)]
                )

            if unit_id in self.unit_cache.get('units', {}):
                previous_status = self.unit_cache['units'][unit_id]
                self.log.info("previous status:" + str(previous_status))
                self.log.info("current status:" + str(state))
                if previous_status != state:
                    # TODO:
                    # self.event("unit {} changed state, it is now: {}".format(unit_id, state))
                    self.event({
                        "event_type": "unit.status.changed",
                        "msg_title": "unit {} changed state".format(unit_id),
                        "msg_text": "it is now: {}".format(state),
                        "tags": ["unit:status_changed"]
                    })
                    self.unit_cache['units'][unit_id] = state
                
            else:
                self.unit_cache['units'][unit_id] = state

        except pystemd.dbusexc.DBusInvalidArgsError as e:
            self.log.info("Unit name invalid for {}".format(unit_id))

    def get_number_processes(self, unit_id):
        try:
            unit = Unit(unit_id, _autoload=True)
            list_processes = unit.Service.GetProcesses()
            process_number = len(list_processes)
            self.gauge('systemd.unit.numprocess', process_number)

        except pystemd.dbusexc.DBusInvalidArgsError as e:
            self.log.info("Unit name invalid for {}".format(unit_id))
