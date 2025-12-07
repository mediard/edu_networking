from ncclient import manager
import xml.dom.minidom as md

HOST = "netconf"
PORT = 830
USER = "netconf"
PASS = "netconf"

filter_xml = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name/>
      <enabled/>
    </interface>
  </interfaces>
</filter>
"""

with manager.connect(
    host=HOST,
    port=PORT,
    username=USER,
    password=PASS,
    hostkey_verify=False,
    allow_agent=False,
    look_for_keys=False,
    timeout=10,
) as m:
    reply = m.get_config(source="running", filter=filter_xml)
    print(md.parseString(str(reply)).toprettyxml())
