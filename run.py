import sys
import signal
# from mysql import MySQL
from pprint import pprint
from datetime import datetime
from marklogic import Entity
from marklogic import MarkLogic

def signal_handler(signum, frame):
    print('THANK YOU!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# def get_Environemts(type,doc):
#     # FETCH ENVIRONMENTS FROM MySQL
#     mysql = MySQL()
#     envs = mysql.get_security_environments()
#     pprint(envs)
#     return envs

entityMap = {
    'ASSESSMENT':           { 'NAME': 'assessment',         'GLOBAL': False },
    'CHECKLIST':            { 'NAME': 'checklist',          'GLOBAL': True },
    'SCOPEDINTERVENTION':   { 'NAME': 'scopedIntervention', 'GLOBAL': True },
    'CLIENTCONTENT':        { 'NAME': 'clientContent',      'GLOBAL': False },
    'GUIDELINE':            { 'NAME': 'guideline',          'GLOBAL': True },
    'IEC':                  { 'NAME': 'iec',                'GLOBAL': True },
    'OUTCOME':              { 'NAME': 'outcome',            'GLOBAL': True },
    'PERFORMANCEMEASURE':   { 'NAME': 'performanceMeasure', 'GLOBAL': True }
}

def analyse_MarkLogic():
    ml = MarkLogic()

    if len(sys.argv) == 1:
        terminate()

    ENTITIES = []
    for i in range(len(sys.argv)):
        if i > 0 and sys.argv[i].upper() in entityMap:
            entity = entityMap[sys.argv[i].upper()]
            ENTITIES.append(Entity(entity['NAME'],entity['GLOBAL']))

    if len(ENTITIES) == 0:
        terminate()
    # ENTITIES = [
    #     Entity('assessment',False),
    #     Entity('checklist',True),
    #     Entity('scopedIntervention',True),
    #     Entity('clientContent',False),
    #     Entity('guideline',True),
    #     Entity('iec',True),
    #     Entity('outcome',True),
    #     Entity('performanceMeasure',True),
    # ]

    try:
        ml.analyse(ENTITIES)
    except Exception as e:
        print('MarkLogic analyse error: %s' % e)
        raise e
    finally:
        print(ml.report)

def terminate():
    print('... please specify the entity from below list,')
    print('... ASSESSMENT|CHECKLIST|SCOPEDINTERVENTION|CLIENTCONTENT|GUIDELINE|IEC|OUTCOME|PERFORMANCEMEASURE')
    exit()

if __name__ == '__main__':
    # START BLOCK
    startTime = datetime.now()

    analyse_MarkLogic()

    # END BLOCK
    endTime = datetime.now()
    delta   = endTime - startTime

    print('\n\n\n')
    print('STARTED AT    : %s' % startTime)
    print('COMPLETED AT  : %s' % endTime)
    print('TOTAL DURATION: %s' % delta)
    # print('TIME REQ : %s ' % delta.total_seconds())