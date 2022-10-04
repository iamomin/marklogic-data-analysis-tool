import re
import sys
import json
import requests
from pprint import pprint
from datetime import datetime
from xmlvalidator import XmlValidator
from xmlvalidator import XsdValidator

ENV_MODE = 'uat' # local | uat| production

ENV_LIST = [1,555,171,281,170,601,485,259,519,337,189,253,511,331,447,493,257,487,177,255,469,99,87,323,134,119,141,307,659,343,619,321,140,461,361,481,467,445,495,285,441,172,611,160,349,479,127,597,295,465,265,317,293,167,615,297,517,325,369,491,505,609,709,1,181,151,355,593,359,124,327,279,507,142,363,183,603,165,299,471,595,275,541,291,341,139,225,585,132,289,367,631,185,135,187,121,351,437,473,305,154,347,713,501,309,477,158,637,155,179,483,513,623,641,146,287,719,613,161,715,147,661,126,523,627,98,133,269,443,509,625,144,605,621,629,633,157,162,150,303,329,665,667,143,156,168,267,283,313,371,451,137,153,159,163,449,463,647,122,164,166,169,282,459,599,653,657,125,249,261,357,635,651,717]
ENV_LIST = [1,555]
ENV_LIST = [517,519,305,447]

class Entity(object):
    """docstring for Entity"""
    def __init__(self, name, isGlobal):
        super(Entity, self).__init__()
        self.name = name
        self.isGlobal = isGlobal

class MarkLogicReport(object):
    """docstring for MarkLogicReport"""

    environmentReport = None
    globalReport = None

    def __init__(self):
        super(MarkLogicReport, self).__init__()
        self.environmentReport = {}
        self.globalReport = {}

    def set_Environment_Data(self,entity,data):
        if entity in self.environmentReport:
            for envId, d in data.items():
                self.environmentReport[entity][envId] = d
        else:
            self.environmentReport[entity] = data

    def set_Global_Data(self,entity,count):
        self.globalReport[entity] = count

    def toString(self):

        netCount = 0
        validNetCount = 0
        invalidNetCount = 0

        # pprint(self.globalReport)
        # pprint(self.environmentReport)

        str = ''

        for entity,eDetails in self.environmentReport.items():
            str += '\n-------------------------------------------------------------------------------------------------------'
            str += '\n- %s analysis by environment' % entity.upper()
            str += '\n-------------------------------------------------------------------------------------------------------'
            for envId,count in eDetails.items():
                params = (
                    envId,
                    count['TOTAL'],
                    count['VALID'],
                    round(count['VALID']/count['TOTAL']*100,4),
                    count['INVALID'],
                    round(count['INVALID']/count['TOTAL']*100,4)
                    )

                str += '\n     Environment    : %4s,   Total: %5s,   Valid: %5s [%7s%%],   Invalid: %5s [%7s%%]' % params

                netCount += count['TOTAL']
                validNetCount += count['VALID']
                invalidNetCount += count['INVALID']

        if netCount > 0:
            params = (
                validNetCount,
                round(validNetCount/netCount*100,4),
                invalidNetCount,
                round(invalidNetCount/netCount*100,4)
                )

            str += '\n\n'
            str += '\n-------------------------------------------------------------------------------------------------------'
            str += '\n- Environment analysis summary'
            str += '\n-------------------------------------------------------------------------------------------------------'
            str += '\n     Total Valid : %5s [%7s%%], Total Invalid : %5s [%7s%%]' % params

        finalCount = netCount
        finalValidNetCount = validNetCount
        finalInvalidNetCount = invalidNetCount

        if len(self.globalReport) > 0:
            str += '\n\n'
            str += '\n*******************************************************************************************************'
            str += '\n* Global entity analysis'
            str += '\n*******************************************************************************************************'

            netCount = 0
            validNetCount = 0
            invalidNetCount = 0

            for entity,count in self.globalReport.items():
                params = (
                    entity.upper(),
                    count['TOTAL'],
                    count['VALID'],
                    round(count['VALID']/count['TOTAL']*100,4),
                    count['INVALID'],
                    round(count['INVALID']/count['TOTAL']*100,4)
                    )
                str += '\n     - %-19s, Total: %5s,   Valid: %5s [%7s%%],   Invalid: %5s [%7s%%]' % params

                netCount += count['TOTAL']
                validNetCount += count['VALID']
                invalidNetCount += count['INVALID']

            if netCount > 0:
                params = (
                    validNetCount,
                    round(validNetCount/netCount*100,4),
                    invalidNetCount,
                    round(invalidNetCount/netCount*100,4)
                    )
                str += '\n\n'
                str += '\n-------------------------------------------------------------------------------------------------------'
                str += '\n- Global data analysis summary'
                str += '\n-------------------------------------------------------------------------------------------------------'
                str += '\n     Valid Percent  : %5s [%7s%%],       Invalid Percent    : %5s [%7s%%]' % params

        finalCount += netCount
        finalValidNetCount += validNetCount
        finalInvalidNetCount += invalidNetCount

        if finalCount > 0:
            str += '\n\n'
            str += '\n#######################################################################################################'
            str += '\n# Final analysis summary'
            str += '\n#######################################################################################################'
            str += '\n     Overall Total Documents   : %5s' % finalCount
            str += '\n     Overall Valid Documents   : %5s [%7s%%]' % (finalValidNetCount,round(finalValidNetCount/finalCount*100,4))
            str += '\n     Overall Invalid Documents : %5s [%7s%%]' % (finalInvalidNetCount,round(finalInvalidNetCount/finalCount*100,4))

        return str

    def __repr__(self):
        return self.toString()

    def __str__(self):
        return self.toString()

class MarkLogic(object):

    validconf = None

    sid     = None
    qid     = None
    crid    = None
    cache   = None
    nc      = None
    nonce   = None
    response= None
    opaque  = None
    cnonce  = None

    env         = ENV_MODE
    uri         = '/qconsole/endpoints/evaler.xqy'
    port        = '8000'
    url         = None
    headers     = None
    querystring = None

    report       = None
    documentCount= None

    validFile   = None
    invalidFile = None

    validEnvs   = ENV_LIST

    def __init__(self):

        try:
            self.set_Properties()
        except Exception as e:
            return

        self.url = "http://localhost:%s%s" % (self.port,self.uri)

        self.querystring = {
            "sid":  self.sid,
            "qid":  self.qid,
            "crid": self.crid,
            "dirty":"true",
            "action":"eval",
            "querytype":"xquery",
            "cache": self.cache
            }

        URI  = '%s?sid=%s&qid=%s&crid=%s&action=eval&querytype=xquery&cache=%s' % (self.uri,self.sid, self.qid, self.crid, self.cache)
        auth = 'Digest username="admin", realm="public", nonce="%s", uri="%s", response="%s", opaque="%s", qop=auth, nc=%s, cnonce="%s"' % (self.nonce, URI, self.response, self.opaque, self.nc, self.cnonce)
        self.headers = {
            'authorization': auth,
            'content-type': "text/plain",
            'Content-Length': '0',
            'connection': "keep-alive",
            'cache-control': "no-cache",
            'X-Requested-With': 'XMLHttpRequest'
            }

        self.report = MarkLogicReport()
        self.documentCount = 0

        self.open_Files()

    def set_Properties(self):

        try:
            with open('.env', 'r') as f:
                envs = json.load(f)
        except Exception as e:
            raise e

        data = envs[self.env]

        self.sid     = data['sid']
        self.qid     = data['qid']
        self.crid    = data['crid']
        self.cache   = data['cache']
        self.nc      = data['nc']
        self.nonce   = data['nonce']
        self.response= data['response']
        self.opaque  = data['opaque']
        self.cnonce  = data['cnonce']
        self.port    = data['port']

        self.validconf = True

    def open_Files(self):
        # Open file handles
        now = datetime.now().strftime('%Y%b%dT%H%M%S')
        vFL = now + '_valid.txt'
        iFL = now + '_invalid.txt'
        self.validFile   = open('log/%s' % vFL, 'w')
        self.invalidFile = open('log/%s' % iFL, 'w')

    def execute(self,query):
        payload = query
        # payload = "fn:doc('/env/1/assessment/f69227dc-da70-4675-9eac-62bbcc750d2e.xml')"

        # print(self.headers)
        response = None
        result = []

        try:
            response = requests.request("POST", self.url, data=payload, headers=self.headers, params=self.querystring)
        except Exception as e:
            print('Query %s Error: %s' % (query,e))
        else:
            # print(response.text)
            if len(response.text) > 0:
                JSON = response.json()
                # print(JSON)
                for data in JSON:
                    result.append(data['result'])

        # print(result)
        return result

    def analyse(self,ENTITIES):

        if self.validconf == None:
            print('... invalid credentials :(')
            return

        for entity in ENTITIES:
            self.validate_Entity(entity)

    def validate_Entity(self,entity):
        # FETCH ALL MATCHING XML URIs
        print('\n.. fetching %s document URLs' % entity.name)
        sys.stdout.flush()

        if entity.isGlobal:
            allDocUris = self.execute("cts:uri-match('*/%s/*.xml')" % entity.name)
            self.validate_Entity_XMLs(entity,allDocUris)
        else:
            for envId in self.validEnvs:
                allDocUris = self.execute("cts:uri-match('/env/%s/%s/*.xml')" % (envId,entity.name))
                self.validate_Entity_XMLs(entity,allDocUris,envId)

    def validate_Entity_XMLs(self,entity,allDocUris,envId=None):
        # XML Validation against schema

        if len(allDocUris) == 0:
            return

        if entity.isGlobal:
            print('\n.. validating %s' % entity.name)
        else:
            print('\n.. validating %s for environment %s' % (entity.name,envId))

        # xv = XmlValidator(entity.name)
        xv = XsdValidator(entity.name)

        print('')

        if xv.ready:

            count = None
            reportData = {}

            for docURL in allDocUris:

                if self.not_Valid_To_Process(entity,docURL):
                    continue

                xmlDoc  = self.get_XML_Doc(docURL)
                isValid = xv.is_Valid(xmlDoc)

                if entity.isGlobal:
                    if count is None:
                        count = { 'VALID': 0, 'INVALID': 0, 'TOTAL': 0 }
                else:
                    parts = docURL.split('/')
                    parsedEnvId = parts[2] if parts[1] == 'env' else '0'
                    if parsedEnvId not in reportData:
                        reportData[parsedEnvId] = { 'VALID': 0, 'INVALID': 0, 'TOTAL': 0 }
                    count = reportData[parsedEnvId]

                t = 'VALID' if isValid else 'INVALID'
                count[t] += 1
                count['TOTAL'] += 1

                self.documentCount += 1
                print('.. %5s: %7s doc %s' % (self.documentCount, ('VALID' if isValid else 'INVALID'), docURL))
                sys.stdout.flush()

                # record urls into file
                self.log(isValid,docURL)

            if entity.isGlobal:
                self.report.set_Global_Data(entity.name,count)
            else:
                self.report.set_Environment_Data(entity.name,reportData)

        xv = None

    def not_Valid_To_Process(self,entity,docURL):
        notValid = False
        if entity.name == 'clientContent' and re.search('staging',docURL):
            notValid = True
        return notValid

    def get_XML_Doc(self,docURL):
        # FETCH XML DATA From URL
        # print(docURL)
        data = self.execute("fn:doc('%s')" % docURL)
        xmlDoc = data[0] if len(data) > 0 else None
        # print(xmlDoc)
        # xmlDoc = re.sub('\n\s+','',xmlDoc) if xmlDoc is not None else '010101'
        xmlDoc = re.sub('<\?xml version="1.0" encoding="UTF-8"\?>\n','',xmlDoc) if xmlDoc is not None else '010101'
        xmlDoc = re.sub('xml:base=".+xml"', '', xmlDoc)
        xmlDoc = re.sub('xmlns:xsi=".+"', '', xmlDoc)
        xmlDoc = re.sub(r'&([^a-zA-Z#])', r'&amp;\1', xmlDoc)
        # print('|%s|' % xmlDoc)
        return xmlDoc

    def log(self,isValid,docURL):
        msg = '%5s: %s\n' % (self.documentCount, docURL)
        if isValid:
            self.validFile.write(msg)
        else:
            self.invalidFile.write(msg)