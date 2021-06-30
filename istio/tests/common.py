# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

CHECK_NAME = 'istio'

MOCK_V2_MESH_INSTANCE = {
    'istio_mesh_endpoint': 'http://localhost:15090/metrics',
    'use_openmetrics': True,
}

MOCK_LEGACY_MESH_INSTANCE = {
    'istio_mesh_endpoint': 'http://localhost:15090/metrics',
}

MOCK_V2_ISTIOD_INSTANCE = {
    'istiod_endpoint': 'http://localhost:8080/metrics',
    'use_openmetrics': True,
}

MOCK_LEGACY_ISTIOD_INSTANCE = {'istiod_endpoint': 'http://localhost:8080/metrics'}

LEGACY_MESH_METRICS = [
    'istio.mesh.request.count',
    'istio.mesh.request.size.count',
    'istio.mesh.request.size.sum',
    'istio.mesh.response.size.count',
    'istio.mesh.response.size.sum',
    # Counts submitted with `send_monotonic_with_gauge`
    'istio.mesh.request.count.total',
    'istio.mesh.request.size.count.total',
    'istio.mesh.request.size.sum.total',
    'istio.mesh.response.size.count.total',
    'istio.mesh.response.size.sum.total',
]


MESH_MERICS_1_5 = [
    'istio.mesh.request.duration.milliseconds.count',
    'istio.mesh.request.duration.milliseconds.sum',
    # TCP Metrics are supported in post 1.4 istio fixture
    'istio.mesh.tcp.connections_closed.total',
    'istio.mesh.tcp.connections_opened.total',
    'istio.mesh.tcp.received_bytes.total',
    'istio.mesh.tcp.send_bytes.total',
    # Counts submitted with `send_monotonic_with_gauge`
    'istio.mesh.request.duration.milliseconds.count.total',
    'istio.mesh.request.duration.milliseconds.sum.total',
    'istio.mesh.tcp.connections_closed.total.total',
    'istio.mesh.tcp.connections_opened.total.total',
    'istio.mesh.tcp.received_bytes.total.total',
    'istio.mesh.tcp.send_bytes.total.total',
]

MESH_METRICS_MAPPER = {
    'istio_request_duration_milliseconds': 'request.duration.milliseconds',
    'istio_request_count': 'request.count',
    'istio_request_duration': 'request.duration',
    'istio_request_size': 'request.size',
    'istio_response_size': 'response.size',
    'istio_requests_total': 'request.count',
    'istio_request_duration_seconds': 'request.duration',
    'istio_request_bytes': 'request.size',
    'istio_response_bytes': 'response.size',
    'istio_tcp_connections_closed_total': 'tcp.connections_closed.total',
    'istio_tcp_connections_opened_total': 'tcp.connections_opened.total',
    'istio_tcp_received_bytes_total': 'tcp.received_bytes.total',
    'istio_tcp_sent_bytes_total': 'tcp.send_bytes.total',
    'istio_request_messages_total': 'request.messages.total',
    'istio_response_messages_total': 'response.messages.total',
}


ISTIOD_METRICS = [
    'istio.citadel.server.root_cert_expiry_timestamp',
    'istio.galley.endpoint_no_pod',
    'istio.galley.validation.config_update_error',
    'istio.galley.validation.config_update',
    'istio.galley.validation.failed',
    'istio.go.gc_duration_seconds.quantile',
    'istio.go.gc_duration_seconds.sum',
    'istio.go.gc_duration_seconds.count',
    'istio.go.goroutines',
    'istio.go.info',
    'istio.go.memstats.alloc_bytes',
    'istio.go.memstats.alloc_bytes_total',
    'istio.go.memstats.buck_hash_sys_bytes',
    'istio.go.memstats.frees_total',
    'istio.go.memstats.gc_cpu_fraction',
    'istio.go.memstats.gc_sys_bytes',
    'istio.go.memstats.heap_alloc_bytes',
    'istio.go.memstats.heap_idle_bytes',
    'istio.go.memstats.heap_inuse_bytes',
    'istio.go.memstats.heap_objects',
    'istio.go.memstats.heap_released_bytes',
    'istio.go.memstats.heap_sys_bytes',
    'istio.go.memstats.last_gc_time_seconds',
    'istio.go.memstats.lookups_total',
    'istio.go.memstats.mallocs_total',
    'istio.go.memstats.mcache_inuse_bytes',
    'istio.go.memstats.mcache_sys_bytes',
    'istio.go.memstats.mspan_inuse_bytes',
    'istio.go.memstats.mspan_sys_bytes',
    'istio.go.memstats.next_gc_bytes',
    'istio.go.memstats.other_sys_bytes',
    'istio.go.memstats.stack_inuse_bytes',
    'istio.go.memstats.stack_sys_bytes',
    'istio.go.memstats.sys_bytes',
    'istio.go.threads',
    'istio.grpc.server.handled_total',
    'istio.grpc.server.handling_seconds.count',
    'istio.grpc.server.handling_seconds.sum',
    'istio.grpc.server.msg_received_total',
    'istio.grpc.server.msg_sent_total',
    'istio.grpc.server.started_total',
    'istio.pilot.conflict.inbound_listener',
    'istio.pilot.conflict.outbound_listener.http_over_current_tcp',
    'istio.pilot.conflict.outbound_listener.http_over_https',
    'istio.pilot.conflict.outbound_listener.tcp_over_current_http',
    'istio.pilot.conflict.outbound_listener.tcp_over_current_tcp',
    'istio.pilot.destrule_subsets',
    'istio.pilot.duplicate_envoy_clusters',
    'istio.pilot.eds_no_instances',
    'istio.pilot.endpoint_not_ready',
    'istio.pilot.inbound_updates',
    'istio.pilot.k8s.cfg_events',
    'istio.pilot.k8s.reg_events',
    'istio.pilot.no_ip',
    'istio.pilot.proxy_convergence_time.count',
    'istio.pilot.proxy_convergence_time.sum',
    'istio.pilot.proxy_queue_time.count',
    'istio.pilot.proxy_queue_time.sum',
    'istio.pilot.push.triggers',
    'istio.pilot.services',
    'istio.pilot.virt_services',
    'istio.pilot.vservice_dup_domain',
    'istio.pilot.xds',
    'istio.pilot.xds.eds_all_locality_endpoints',
    'istio.pilot.xds.eds_instances',
    'istio.pilot.xds.push.time.count',
    'istio.pilot.xds.push.time.sum',
    'istio.pilot.xds.pushes',
    'istio.process.cpu_seconds_total',
    'istio.process.max_fds',
    'istio.process.open_fds',
    'istio.process.resident_memory_bytes',
    'istio.process.start_time_seconds',
    'istio.process.virtual_memory_bytes',
    'istio.process.virtual_memory_max_bytes',
    'istio.sidecar_injection.requests_total',
    'istio.sidecar_injection.success_total',
]

V2_MESH_METRICS = [
    'istio.mesh.tcp.connections_closed.count',
    'istio.mesh.tcp.send_bytes.count',
    'istio.mesh.tcp.connections_opened.count',
    'istio.mesh.tcp.received_bytes.count',
    'istio.mesh.request.count',
    'istio.mesh.request.duration.milliseconds.bucket',
    'istio.mesh.request.duration.milliseconds.sum',
    'istio.mesh.request.duration.milliseconds.count',
    'istio.mesh.response.size.bucket',
    'istio.mesh.response.size.sum',
    'istio.mesh.response.size.count',
    'istio.mesh.request.size.bucket',
    'istio.mesh.request.size.sum',
    'istio.mesh.request.size.count',
]

ISTIOD_V2_METRICS = [
    'istio.citadel.server.root_cert_expiry_timestamp',
    'istio.galley.endpoint_no_pod',
    'istio.galley.validation.config_update_error.count',
    'istio.galley.validation.config_update.count',
    'istio.galley.validation.failed.count',
    'istio.go.gc_duration_seconds.quantile',
    'istio.go.gc_duration_seconds.sum',
    'istio.go.gc_duration_seconds.count',
    'istio.go.goroutines',
    'istio.go.info',
    'istio.go.memstats.alloc_bytes',
    'istio.go.memstats.buck_hash_sys_bytes',
    'istio.go.memstats.frees.count',
    'istio.go.memstats.gc_cpu_fraction',
    'istio.go.memstats.gc_sys_bytes',
    'istio.go.memstats.heap_alloc_bytes',
    'istio.go.memstats.heap_idle_bytes',
    'istio.go.memstats.heap_inuse_bytes',
    'istio.go.memstats.heap_objects',
    'istio.go.memstats.heap_released_bytes',
    'istio.go.memstats.heap_sys_bytes',
    'istio.go.memstats.last_gc_time_seconds',
    'istio.go.memstats.lookups.count',
    'istio.go.memstats.mallocs.count',
    'istio.go.memstats.mcache_inuse_bytes',
    'istio.go.memstats.mcache_sys_bytes',
    'istio.go.memstats.mspan_inuse_bytes',
    'istio.go.memstats.mspan_sys_bytes',
    'istio.go.memstats.next_gc_bytes',
    'istio.go.memstats.other_sys_bytes',
    'istio.go.memstats.stack_inuse_bytes',
    'istio.go.memstats.stack_sys_bytes',
    'istio.go.memstats.sys_bytes',
    'istio.go.threads',
    'istio.grpc.server.handled.count',
    'istio.grpc.server.handling_seconds.bucket',
    'istio.grpc.server.handling_seconds.sum',
    'istio.grpc.server.handling_seconds.count',
    'istio.grpc.server.msg_received.count',
    'istio.grpc.server.msg_sent.count',
    'istio.grpc.server.started.count',
    'istio.pilot.conflict.inbound_listener',
    'istio.pilot.conflict.outbound_listener.http_over_current_tcp',
    'istio.pilot.conflict.outbound_listener.http_over_https',
    'istio.pilot.conflict.outbound_listener.tcp_over_current_http',
    'istio.pilot.conflict.outbound_listener.tcp_over_current_tcp',
    'istio.pilot.destrule_subsets',
    'istio.pilot.duplicate_envoy_clusters',
    'istio.pilot.eds_no_instances',
    'istio.pilot.endpoint_not_ready',
    'istio.pilot.inbound_updates.count',
    'istio.pilot.k8s.cfg_events.count',
    'istio.pilot.k8s.reg_events.count',
    'istio.pilot.no_ip',
    'istio.pilot.proxy_convergence_time.bucket',
    'istio.pilot.proxy_convergence_time.sum',
    'istio.pilot.proxy_convergence_time.count',
    'istio.pilot.proxy_queue_time.bucket',
    'istio.pilot.proxy_queue_time.sum',
    'istio.pilot.proxy_queue_time.count',
    'istio.pilot.push.triggers.count',
    'istio.pilot.services',
    'istio.pilot.virt_services',
    'istio.pilot.vservice_dup_domain',
    'istio.pilot.xds',
    'istio.pilot.xds.eds_all_locality_endpoints',
    'istio.pilot.xds.eds_instances',
    'istio.pilot.xds.push.time.bucket',
    'istio.pilot.xds.push.time.sum',
    'istio.pilot.xds.push.time.count',
    'istio.pilot.xds.pushes.count',
    'istio.process.cpu_seconds.count',
    'istio.process.max_fds',
    'istio.process.open_fds',
    'istio.process.resident_memory_bytes',
    'istio.process.start_time_seconds',
    'istio.process.virtual_memory_bytes',
    'istio.process.virtual_memory_max_bytes',
    'istio.sidecar_injection.requests.count',
    'istio.sidecar_injection.success.count',
]
