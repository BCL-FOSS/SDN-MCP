from fastmcp import FastMCP
from sdn_tools.UniFiNetAPI import UniFiNetAPI

mcp = FastMCP(name="UniFiAutomation")

@mcp.tool
async def active_clients(api: str, cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.active_clients(site=site)

@mcp.tool
async def active_routes(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.active_routes()

@mcp.tool
async def alarm_data(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.alarm_data()

@mcp.tool
async def all_clients(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.all_clients()

@mcp.tool
async def auth_audit(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.auth_audit()

@mcp.tool
async def client_dpi_data(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.client_dpi_data

@mcp.tool
async def controller_health_data(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.controller_health_data()

@mcp.tool
async def device_data(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.device_data()

@mcp.tool
async def dynamic_dns_config(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.dynamic_dns_config()

@mcp.tool
async def dynamic_dns_info(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.dynamic_dns_info()

@mcp.tool
async def event_data(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.event_data()

@mcp.tool
async def firewall_groups(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.firewall_groups()

@mcp.tool
async def firewall_rules(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.firewall_rules()

@mcp.tool
async def get_system_info(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.get_sysinfo()

@mcp.tool
async def list_port_profiles(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.list_port_profiles()

@mcp.tool
async def manage_clients(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.mgr_clients()

@mcp.tool
async def manage_devices(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.mgr_devices()

@mcp.tool
async def manage_sites(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.mgr_sites()

@mcp.tool
async def port_forwards(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.port_forwards()

@mcp.tool
async def radius_accounts(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.radius_accounts()

@mcp.tool
async def radius_profiles(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.radius_profiles()

@mcp.tool
async def reports(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.reports()

@mcp.tool
async def rf_scan_results(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.rf_scan_results()

@mcp.tool
async def rogue_aps(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.rogue_aps()

@mcp.tool
async def site_dpi_data(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.site_dpi_data()

@mcp.tool
async def site_settings(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.site_settings()

@mcp.tool
async def site_stats(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.site_stats()

@mcp.tool
async def sites(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.sites()

@mcp.tool
async def udm_poweroff(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.udm_poweroff()

@mcp.tool
async def udm_reboot(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.udm_reboot()

@mcp.tool
async def wlans(cntlr_data:dict, opt: dict) -> dict:
    ubnt = UniFiNetAPI()
    auth_rslt = await ubnt.authenticate()
    site = opt.get('site')
    await ubnt.wlans()

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=4200,
        log_level="debug",
    )