from fastmcp import FastMCP
from sdn_tools.UniFiNetAPI import UniFiNetAPI

mcp = FastMCP(name="SDNAutomationServer")

@mcp.tool
async def ubnt(api: str, cntlr_data:dict, opt: dict) -> dict:

    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    match api:
        case 'active_clients':
            await ubnt.active_clients(site=site)
        case 'active_routes':
            await ubnt.active_routes()
        case 'alarms':
            await ubnt.alarm_data()
        case 'clients':
            await ubnt.all_clients()
        case 'auth_audit':
            await ubnt.auth_audit()
        case 'client_dpi':
            await ubnt.client_dpi_data()
        case 'controller_health':
            await ubnt.controller_health_data()
        case 'device_data':
            await ubnt.device_data()
        case 'device_data_basic':
            await ubnt.device_data_basic()
        case 'dns_cnfg':
            await ubnt.dynamic_dns_config()
        case 'dns_info':
            await ubnt.dynamic_dns_info()
        case 'events':
            await ubnt.event_data()
        case 'fw_groups':
            await ubnt.firewall_groups()
        case 'fw_rules':
            await ubnt.firewall_rules()
        case 'sysinfo':
            await ubnt.get_sysinfo()
        case 'port_prfs':
            await ubnt.list_port_profiles()
        case 'mgr_clnts':
            await ubnt.mgr_clients()
        case 'mgr_devs':
            await ubnt.mgr_devices()
        case 'mgr_sts':
            await ubnt.mgr_sites()
        case 'port_fwds':
            await ubnt.port_forwards()
        case 'radius_accts':
            await ubnt.radius_accounts()
        case 'radius_prfs':
            await ubnt.radius_profiles()
        case 'reports':
            await ubnt.reports()
        case 'rf_scans':
            await ubnt.rf_scan_results()
        case 'rogue_aps':
            await ubnt.rogue_aps()
        case 'site_dpi':
            await ubnt.site_dpi_data()
        case 'site_settings':
            await ubnt.site_settings()
        case 'site_stats':
            await ubnt.site_stats()
        case 'sites':
            await ubnt.sites()
        case 'udm_off':
            await ubnt.udm_poweroff()
        case 'udm_cycle':
            await ubnt.udm_reboot()
        case 'wlans':
            await ubnt.wlans()
    return {}

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=4200,
        log_level="debug",
    )