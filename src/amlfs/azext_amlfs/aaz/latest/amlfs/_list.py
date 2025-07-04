# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "amlfs list",
)
class List(AAZCommand):
    """List all AML file systems the user has access to under a resource group.

    :example: List amlfs
        az amlfs list -g rg
    """

    _aaz_info = {
        "version": "2023-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.storagecache/amlfilesystems", "2023-05-01"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.storagecache/amlfilesystems", "2023-05-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        condition_1 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        if condition_0:
            self.AmlFilesystemsList(ctx=self.ctx)()
        if condition_1:
            self.AmlFilesystemsListByResourceGroup(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class AmlFilesystemsList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.StorageCache/amlFilesystems",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZIdentityObjectType()
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )
            _element.zones = AAZListType()

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.client_info = AAZObjectType(
                serialized_name="clientInfo",
                flags={"read_only": True},
            )
            properties.encryption_settings = AAZObjectType(
                serialized_name="encryptionSettings",
            )
            properties.filesystem_subnet = AAZStrType(
                serialized_name="filesystemSubnet",
                flags={"required": True},
            )
            properties.health = AAZObjectType(
                flags={"read_only": True},
            )
            properties.hsm = AAZObjectType()
            properties.maintenance_window = AAZObjectType(
                serialized_name="maintenanceWindow",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.storage_capacity_ti_b = AAZFloatType(
                serialized_name="storageCapacityTiB",
                flags={"required": True},
            )
            properties.throughput_provisioned_m_bps = AAZIntType(
                serialized_name="throughputProvisionedMBps",
                flags={"read_only": True},
            )

            client_info = cls._schema_on_200.value.Element.properties.client_info
            client_info.container_storage_interface = AAZObjectType(
                serialized_name="containerStorageInterface",
                flags={"read_only": True},
            )
            client_info.lustre_version = AAZStrType(
                serialized_name="lustreVersion",
                flags={"read_only": True},
            )
            client_info.mgs_address = AAZStrType(
                serialized_name="mgsAddress",
                flags={"read_only": True},
            )
            client_info.mount_command = AAZStrType(
                serialized_name="mountCommand",
                flags={"read_only": True},
            )

            container_storage_interface = cls._schema_on_200.value.Element.properties.client_info.container_storage_interface
            container_storage_interface.persistent_volume = AAZStrType(
                serialized_name="persistentVolume",
                flags={"read_only": True},
            )
            container_storage_interface.persistent_volume_claim = AAZStrType(
                serialized_name="persistentVolumeClaim",
                flags={"read_only": True},
            )
            container_storage_interface.storage_class = AAZStrType(
                serialized_name="storageClass",
                flags={"read_only": True},
            )

            encryption_settings = cls._schema_on_200.value.Element.properties.encryption_settings
            encryption_settings.key_encryption_key = AAZObjectType(
                serialized_name="keyEncryptionKey",
            )

            key_encryption_key = cls._schema_on_200.value.Element.properties.encryption_settings.key_encryption_key
            key_encryption_key.key_url = AAZStrType(
                serialized_name="keyUrl",
                flags={"required": True},
            )
            key_encryption_key.source_vault = AAZObjectType(
                serialized_name="sourceVault",
                flags={"required": True},
            )

            source_vault = cls._schema_on_200.value.Element.properties.encryption_settings.key_encryption_key.source_vault
            source_vault.id = AAZStrType()

            health = cls._schema_on_200.value.Element.properties.health
            health.state = AAZStrType()
            health.status_code = AAZStrType(
                serialized_name="statusCode",
            )
            health.status_description = AAZStrType(
                serialized_name="statusDescription",
            )

            hsm = cls._schema_on_200.value.Element.properties.hsm
            hsm.archive_status = AAZListType(
                serialized_name="archiveStatus",
                flags={"read_only": True},
            )
            hsm.settings = AAZObjectType()

            archive_status = cls._schema_on_200.value.Element.properties.hsm.archive_status
            archive_status.Element = AAZObjectType(
                flags={"read_only": True},
            )

            _element = cls._schema_on_200.value.Element.properties.hsm.archive_status.Element
            _element.filesystem_path = AAZStrType(
                serialized_name="filesystemPath",
                flags={"read_only": True},
            )
            _element.status = AAZObjectType(
                flags={"read_only": True},
            )

            status = cls._schema_on_200.value.Element.properties.hsm.archive_status.Element.status
            status.error_code = AAZStrType(
                serialized_name="errorCode",
                flags={"read_only": True},
            )
            status.error_message = AAZStrType(
                serialized_name="errorMessage",
                flags={"read_only": True},
            )
            status.last_completion_time = AAZStrType(
                serialized_name="lastCompletionTime",
                flags={"read_only": True},
            )
            status.last_started_time = AAZStrType(
                serialized_name="lastStartedTime",
                flags={"read_only": True},
            )
            status.percent_complete = AAZIntType(
                serialized_name="percentComplete",
                flags={"read_only": True},
            )
            status.state = AAZStrType(
                flags={"read_only": True},
            )

            settings = cls._schema_on_200.value.Element.properties.hsm.settings
            settings.container = AAZStrType(
                flags={"required": True},
            )
            settings.import_prefix = AAZStrType(
                serialized_name="importPrefix",
            )
            settings.logging_container = AAZStrType(
                serialized_name="loggingContainer",
                flags={"required": True},
            )

            maintenance_window = cls._schema_on_200.value.Element.properties.maintenance_window
            maintenance_window.day_of_week = AAZStrType(
                serialized_name="dayOfWeek",
            )
            maintenance_window.time_of_day_utc = AAZStrType(
                serialized_name="timeOfDayUTC",
            )

            sku = cls._schema_on_200.value.Element.sku
            sku.name = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            zones = cls._schema_on_200.value.Element.zones
            zones.Element = AAZStrType()

            return cls._schema_on_200

    class AmlFilesystemsListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageCache/amlFilesystems",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZIdentityObjectType()
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )
            _element.zones = AAZListType()

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.client_info = AAZObjectType(
                serialized_name="clientInfo",
                flags={"read_only": True},
            )
            properties.encryption_settings = AAZObjectType(
                serialized_name="encryptionSettings",
            )
            properties.filesystem_subnet = AAZStrType(
                serialized_name="filesystemSubnet",
                flags={"required": True},
            )
            properties.health = AAZObjectType(
                flags={"read_only": True},
            )
            properties.hsm = AAZObjectType()
            properties.maintenance_window = AAZObjectType(
                serialized_name="maintenanceWindow",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.storage_capacity_ti_b = AAZFloatType(
                serialized_name="storageCapacityTiB",
                flags={"required": True},
            )
            properties.throughput_provisioned_m_bps = AAZIntType(
                serialized_name="throughputProvisionedMBps",
                flags={"read_only": True},
            )

            client_info = cls._schema_on_200.value.Element.properties.client_info
            client_info.container_storage_interface = AAZObjectType(
                serialized_name="containerStorageInterface",
                flags={"read_only": True},
            )
            client_info.lustre_version = AAZStrType(
                serialized_name="lustreVersion",
                flags={"read_only": True},
            )
            client_info.mgs_address = AAZStrType(
                serialized_name="mgsAddress",
                flags={"read_only": True},
            )
            client_info.mount_command = AAZStrType(
                serialized_name="mountCommand",
                flags={"read_only": True},
            )

            container_storage_interface = cls._schema_on_200.value.Element.properties.client_info.container_storage_interface
            container_storage_interface.persistent_volume = AAZStrType(
                serialized_name="persistentVolume",
                flags={"read_only": True},
            )
            container_storage_interface.persistent_volume_claim = AAZStrType(
                serialized_name="persistentVolumeClaim",
                flags={"read_only": True},
            )
            container_storage_interface.storage_class = AAZStrType(
                serialized_name="storageClass",
                flags={"read_only": True},
            )

            encryption_settings = cls._schema_on_200.value.Element.properties.encryption_settings
            encryption_settings.key_encryption_key = AAZObjectType(
                serialized_name="keyEncryptionKey",
            )

            key_encryption_key = cls._schema_on_200.value.Element.properties.encryption_settings.key_encryption_key
            key_encryption_key.key_url = AAZStrType(
                serialized_name="keyUrl",
                flags={"required": True},
            )
            key_encryption_key.source_vault = AAZObjectType(
                serialized_name="sourceVault",
                flags={"required": True},
            )

            source_vault = cls._schema_on_200.value.Element.properties.encryption_settings.key_encryption_key.source_vault
            source_vault.id = AAZStrType()

            health = cls._schema_on_200.value.Element.properties.health
            health.state = AAZStrType()
            health.status_code = AAZStrType(
                serialized_name="statusCode",
            )
            health.status_description = AAZStrType(
                serialized_name="statusDescription",
            )

            hsm = cls._schema_on_200.value.Element.properties.hsm
            hsm.archive_status = AAZListType(
                serialized_name="archiveStatus",
                flags={"read_only": True},
            )
            hsm.settings = AAZObjectType()

            archive_status = cls._schema_on_200.value.Element.properties.hsm.archive_status
            archive_status.Element = AAZObjectType(
                flags={"read_only": True},
            )

            _element = cls._schema_on_200.value.Element.properties.hsm.archive_status.Element
            _element.filesystem_path = AAZStrType(
                serialized_name="filesystemPath",
                flags={"read_only": True},
            )
            _element.status = AAZObjectType(
                flags={"read_only": True},
            )

            status = cls._schema_on_200.value.Element.properties.hsm.archive_status.Element.status
            status.error_code = AAZStrType(
                serialized_name="errorCode",
                flags={"read_only": True},
            )
            status.error_message = AAZStrType(
                serialized_name="errorMessage",
                flags={"read_only": True},
            )
            status.last_completion_time = AAZStrType(
                serialized_name="lastCompletionTime",
                flags={"read_only": True},
            )
            status.last_started_time = AAZStrType(
                serialized_name="lastStartedTime",
                flags={"read_only": True},
            )
            status.percent_complete = AAZIntType(
                serialized_name="percentComplete",
                flags={"read_only": True},
            )
            status.state = AAZStrType(
                flags={"read_only": True},
            )

            settings = cls._schema_on_200.value.Element.properties.hsm.settings
            settings.container = AAZStrType(
                flags={"required": True},
            )
            settings.import_prefix = AAZStrType(
                serialized_name="importPrefix",
            )
            settings.logging_container = AAZStrType(
                serialized_name="loggingContainer",
                flags={"required": True},
            )

            maintenance_window = cls._schema_on_200.value.Element.properties.maintenance_window
            maintenance_window.day_of_week = AAZStrType(
                serialized_name="dayOfWeek",
            )
            maintenance_window.time_of_day_utc = AAZStrType(
                serialized_name="timeOfDayUTC",
            )

            sku = cls._schema_on_200.value.Element.sku
            sku.name = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            zones = cls._schema_on_200.value.Element.zones
            zones.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
