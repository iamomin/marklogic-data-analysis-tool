import os
import io
from lxml import etree
from pprint import pprint

class XmlValidator(object):

    schema  = None
    dtd     = None
    ready   = False

    """docstring for XmlValidator"""
    def __init__(self, schema_name):
        super(XmlValidator, self).__init__()
        self.schema = schema_name
        dtd_file = 'data/dtd/%s.dtd' % self.schema
        # print(dtd_file)

        if os.path.exists(dtd_file):
            try:
                self.dtd = etree.DTD(dtd_file)
                self.ready = True
                print('.. using DTD: %s' % dtd_file)
            except Exception as e:
                print('DTD file error: %s' % e)
        else:
            self.ready = False
            print('.. DTD for %s not exist' % schema_name.upper())

    def is_Valid(self,xml_Doc):
        # print(xml_Doc)
        root = etree.XML(xml_Doc)
        result = self.dtd.validate(root)
        # print('Is Valid: %s' % result)
        return result

class XsdValidator(object):
    schema  = None
    xsd     = None
    ready   = None

    """docstring for XsdValidator"""
    def __init__(self, schema_name):
        super(XsdValidator, self).__init__()
        self.schema = schema_name
        xsd_file = 'data/xsd/%s.xsd' % self.schema
        # print(xsd_file)

        if os.path.exists(xsd_file):
            try:
                xmlschema_doc = etree.parse(xsd_file)
                self.xsd = etree.XMLSchema(xmlschema_doc)
                self.ready = True
                # print('.. using XSD: %s' % xsd_file)
            except Exception as e:
                print('XSD file error: %s' % e)
        else:
            print('.. XSD for %s not exist' % self.schema.upper())
            self.ready = False

    def is_Valid(self,xml_Doc):
        doc = etree.parse(io.StringIO(xml_Doc))
        result = self.xsd.validate(doc)
        # print('XSD check, Is Valid: %s' % result)
        return result

TTT = '''<assessment>
    <id/>
    <name>Heart Failure + Meditech 12</name>
    <parentId/>
    <documents>
        <document>
            <id>bf93765a-992b-43b8-b1c7-eddd40a13eb4</id>
            <version>1</version>
        </document>
    </documents>
    <checklistId>074f1d33-8899-43ea-af50-8110b5ce36b2</checklistId>
    <checklistVersion>2</checklistVersion>
    <created>
        <userId>368</userId>
        <dateTime>2017-11-20T11:00:45Z</dateTime>
    </created>
    <caresetting>Inpatient</caresetting>
    <status>Assess</status>
    <scopedInterventions>
        <scopedIntervention>
            <id>64e5e305-5efb-47cb-ae01-f372766070d3</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>e82fe2cd-c7bb-4d82-b5ee-b9018338cd9d</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>123d8706-409c-4a5d-935a-9618ee3d20f6</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>63e4f9a5-500c-4714-84e4-6960ca5a3a3f</id>
            <matches>
                <segment>
                    <id>t26_8-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>AVOID routine invasive hemodynamic monitoring in normotensive, acutely decompensated HF  congestion responding well</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>cc969043-25ae-41ac-a9ce-8a9669122bfe</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>4b0f9330-76c0-4935-9e20-835e779f498b</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>b7f4aa65-90c4-4332-b04a-1dcd4125d13d</id>
            <matches>
                <segment>
                    <id>t1d_1-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Teach Heart Failure</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>6750a25b-4cae-4c9a-af62-bd8a834a710b</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>8fb8a982-5b66-4e87-a72a-fba9741834c4</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>0634309d-4144-4485-a4d9-732e4ed4e838</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>b23283b7-a7c7-4cb0-8d6c-a5d3938c9fe5</id>
            <matches>
                <segment>
                    <id>t17_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Angiotensin-Converting Enzyme Inhibitors</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t19_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>LISINOPRIL TAB 2.5 MG TAB</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t1c_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>LISINOPRIL TAB 5 MG TAB</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t1f_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>RAMIPRIL CAP 2.5 MG CAP</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t1i_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>RAMIPRIL CAP 5 MG CAP</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t1l_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>ENALAPRIL TAB 5 MG TAB</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t1o_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>ENALAPRIL TAB 5 MG TAB</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t22_8-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>AVOID combining aldosterone antagonists, ACE inhibitors,  angiotensin receptor blockers (ARBs) in symptomatic HF </text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>fb280de1-95e9-475a-9ca4-6f5db7d2d674</id>
            <matches>
                <segment>
                    <id>t1r_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Angiotensin Receptor Blockers</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t1s_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>LOSARTAN TAB 25 MG TAB (Cozaar)</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t1v_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>LOSARTAN TAB 50 MG TAB</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>tk_5-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>VALSARTAN TAB 80 MG TAB</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>tn_5-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>VALSARTAN TAB 80 MG TAB</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t22_8-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>AVOID combining aldosterone antagonists, ACE inhibitors,  angiotensin receptor blockers (ARBs) in symptomatic HF </text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>ts_9-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Give an ACE - OR ARB if ACE intolerant, within 24 hours of infarction for prevention of cardiovascular events where LVEF less</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>c955606d-d2e4-4b37-b15f-c5943e17ee5d</id>
            <matches>
                <segment>
                    <id>tz_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Aldosterone Antagonists</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t11_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>SPIRONOLACTONE TAB 25 MG TAB (Aldactone)</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t22_8-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>AVOID combining aldosterone antagonists, ACE inhibitors,  angiotensin receptor blockers (ARBs) in symptomatic HF </text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>f920d3d4-ad5b-474e-8b1c-dda04cf61147</id>
            <matches>
                <segment>
                    <id>tr_5-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>METOPROLOL SUCCINATE XL TAB 25 MG TABCR</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>tw_5-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>CARVEDILOL TAB 12.5 MG TAB</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>5343e784-9570-4b0e-adf0-558963893cd1</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>6300c652-2275-4904-90f5-9623d7e936b7</id>
            <matches>
                <segment>
                    <id>t1z_8-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>AVOID first-generation calcium channel blockers in systolic HF (e.g., diltiazem, verapamil).</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>3312e7c7-426c-4933-b488-446f5d50fe1b</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>0b776a48-9764-4f76-9bf2-4bdaa59fffde</id>
            <matches>
                <segment>
                    <id>ti_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Loop Diuretics</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>tj_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>FUROSEMIDE TAB 20 MG TAB</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>tm_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>FUROSEMIDE TAB 40 MG TAB</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>tp_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>FUROSEMIDE INJ 10 MG/ML ML (Lasix)</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>ts_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Thiazide / Thiazide Like Diuretics</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>tt_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>METOLAZONE TAB 2.5 MG TAB (Zaroxolyn)</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>tw_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>METOLAZONE TAB 5 MG TAB</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t11_4-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>SPIRONOLACTONE TAB 25 MG TAB (Aldactone)</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t29_8-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Thiazide/Thiazide-Like diuretics may not be effective in reduced renal function patients.</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>3b214315-ddb4-4617-9a0d-a937a60f6574</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>f8673fb3-cc56-4da4-84f3-bc2b45866503</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>3ec71363-a868-45fc-9f5e-2826a63dc867</id>
            <matches>
                <segment>
                    <id>tn_9-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Recommend IV inotropics (dopamine, or milrinone) for hypotension with organ hypoperfusion to preserve end-organ</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>2fb88b50-6b53-4a57-9880-258786d3efdb</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>e53794e6-c39d-4454-a320-de31419c5947</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>1ec69066-8b48-4144-9c8b-c59727f193cd</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>605e61f2-225c-4829-b5ad-0d8edd68adc5</id>
            <matches>
                <segment>
                    <id>ty_8-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Troponin I TnI Quant</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t11_8-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Troponin I TnI Quant</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>4c69c84a-90ed-424e-a33c-34c4e2736780</id>
            <matches>
                <segment>
                    <id>t1i_7-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>CBC Diff reflex to Manual Diff</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>53f9c3f4-370e-4f98-b2af-7dc5bf232dcb</id>
            <matches>
                <segment>
                    <id>tq_8-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Lipid Panel</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>bd09153f-b7e9-45b0-8c35-4507f25bd752</id>
            <matches>
                <segment>
                    <id>t1m_7-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Hepatic Func Panel Liver LFP</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>2d89a9dc-e02a-42a9-935c-bb05af239fcd</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>af96f5ca-af43-49d2-b20a-c54247b6164c</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>7d8ce255-5070-4e88-9a8d-c83b9e697b46</id>
            <matches>
                <segment>
                    <id>t1n_3-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Potassium Protocol &gt;/=3.5</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>t1p_3-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Potassium Protocol &gt;/=4.0</text>
                    <durianMatch>true</durianMatch>
                </segment>
                <segment>
                    <id>tj_8-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Basic Metabolic Panel BMP</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>15e75c78-9ab1-4575-b1a0-5e5a16dfaf26</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>90e1f202-e532-4316-b767-9bd0f56a94de</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>b9aba906-0dbb-45f2-a347-7e37b1ca4085</id>
            <matches>
                <segment>
                    <id>tw_3-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>EKG Electrocardiogram</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>b78d15f1-47b4-4231-8fea-6ee4f58bfd42</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>f6acb3bf-c704-4697-9e37-0a3f9e76ce23</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>db73a12d-0c4e-4367-b3d8-949d45450353</id>
            <matches>
                <segment>
                    <id>tr_3-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>DX Chest 2 View PA/Lateral CXR</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>d8e5d623-07e6-4101-ad5d-1f3a8c63b162</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>dda9081c-5a4c-45b6-afb6-f1f4f918e484</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>9f1e0346-6c7e-4fd4-b042-e3ddb1f9a7ea</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>c1d7d1f0-fe7e-4b6c-a6ae-11ea855b5e5b</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>3bd153e9-596b-4510-973e-06b4472b53b6</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>e48785a9-4afc-4070-871b-9d4f7134b97d</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>074e90df-92f8-4f82-ae94-48524e567979</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>86faf5b9-4bab-42e6-b7fb-4ef20f7bf293</id>
            <matches>
                <segment>
                    <id>t1d_3-fa882928-28bc-4dd5-af72-548c52ba0063</id>
                    <text>Cardiac Rehab Consult</text>
                    <durianMatch>true</durianMatch>
                </segment>
            </matches>
        </scopedIntervention>
        <scopedIntervention>
            <id>d15bdcfd-83b1-4ada-a13b-c552df64c968</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>1b41cf73-d638-4c5d-a281-50178306963d</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>d23dad7d-d023-4b34-ba64-525914d8e56c</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>55bf831a-3aca-4dad-b43a-034ab67d2db7</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>a7f67b9a-2abb-4e64-87b8-55b8eed8a5bf</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>bbdfb1d0-4e5f-4407-a4d9-03d4cfcbe916</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>3abdf9c4-05fa-48fd-a601-42d84cadb538</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>c4390e2f-c280-4d0d-8082-5fb5e23473e4</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>dcf5bf4a-65b1-40d5-bc1f-6be67c53429a</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>455e4ffa-9dfb-43ec-8d7a-6d663e61bd85</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>0f6f6049-55cc-40d8-a0c0-27eb6518e5cf</id>
            <matches/>
        </scopedIntervention>
        <scopedIntervention>
            <id>737407e8-342a-401a-9e30-129777d374af</id>
            <matches/>
        </scopedIntervention>
    </scopedInterventions>
</assessment>'''