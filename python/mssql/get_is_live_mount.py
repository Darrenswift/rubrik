import rubrik_cdm
import urllib3

urllib3.disable_warnings()

db_name = 'AdventureWorks2016_EXT'
instance = 'MSSQLSERVER'
hostname = 'em1-promowol-w1.rubrikdemo.com'
effective_sla_domain = '4hr-30d-Azure'

rubrik = rubrik_cdm.Connect(enable_logging=True)

get_db = rubrik.get_sql_db(is_live_mount=True)#, instance=instance hostname=hostname)

print(get_db)
