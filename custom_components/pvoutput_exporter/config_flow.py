"""Config flow for PV Output Exporter."""
from __future__ import annotations

from typing import Any
from homeassistant.helpers.config_validation import boolean

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry, ConfigFlow, OptionsFlow
from homeassistant.const import CONF_NAME, CONF_API_KEY
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult

from .const import CONF_SYSTEM_ID, DOMAIN


class PVOutputExporterFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for PVOutput Exporter."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: ConfigEntry,
    ) -> PVOutputExporterOptionFlowHandler:
        """Get the options flow for this handler."""
        return PVOutputExporterFlowHandler(config_entry)

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle a flow initiated by the user."""
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data = {},
                options={
                    CONF_API_KEY: user_input[CONF_API_KEY],
                    CONF_SYSTEM_ID: user_input[CONF_SYSTEM_ID]
                },
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_NAME, default=self.hass.config.location_name
                    ): str,
                    vol.Required(CONF_API_KEY, default=""): str,
                    vol.Required(CONF_SYSTEM_ID, default=""): str,
                }
            ),
        )


class PVOutputExporterOptionFlowHandler(OptionsFlow):
    """Handle options."""

    def __init__(self, config_entry: ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_API_KEY,
                        default=self.config_entry.options.get(CONF_API_KEY),
                    ): str,
                    vol.Required(
                        CONF_SYSTEM_ID,
                        default=self.config_entry.options.get(CONF_SYSTEM_ID),
                    ): str,

                }
            ),
        )
