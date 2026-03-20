# Changelog

All notable changes to the MCP Server Odoo module will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [19.0.1.0.5] - 2026-03-15

### Fixed

- **odoo.sh Test Compatibility**: Added `@mute_logger` decorators to tests that deliberately trigger error-level logs, preventing false test failures on odoo.sh where ERROR logs are treated as test errors

## [19.0.1.0.4] - 2026-02-25

### Added

- **Session-Based Authentication**: Endpoints now accept Odoo session cookies in addition to API keys, enabling browser-based access
- **Auth Method Reporting**: `/mcp/auth/validate` response includes `auth_method` field (`api_key` or `session`)

### Changed

- Authentication priority: API key → session → 401 (previously API key only)
- Routes changed from `auth="none"` to `auth="public"` for session resolution

### Removed

- **"Require API Keys" setting** (`mcp_server.use_api_keys`): All endpoints now always require a valid API key or session cookie

## [19.0.1.0.3] - 2025-12-13

### Added

- **Initial Release for Odoo 19**: Version of MCP Server module for Odoo 19
- **Security Groups**: MCP Administrator (full access) and MCP User (read-only)
- **Model Configuration**: Enable/disable models with granular permissions (read, write, create, unlink)
- **API Key Authentication**: Secure authentication with rate limiting support
- **REST API Endpoints**:
  - `/mcp/health` - Health check
  - `/mcp/auth/validate` - API key validation
  - `/mcp/system/info` - System information
  - `/mcp/models` - List enabled models
  - `/mcp/models/{model}/access` - Check permissions
- **XML-RPC Controllers**: MCP-specific endpoints with access control
  - `/mcp/xmlrpc/common` - Authentication
  - `/mcp/xmlrpc/object` - Model operations
- **Configuration UI**: Settings integration and model selection wizard
- **Audit Logging**: Comprehensive operation tracking with built-in viewer
- **Data Models**:
  - `mcp.enabled.model` - Model access configuration
  - `mcp.log` - Audit trail

### Technical Details
- Compatible with Odoo 19.0
- Follows Odoo module best practices
- Extensive test coverage
- Full documentation and type hints