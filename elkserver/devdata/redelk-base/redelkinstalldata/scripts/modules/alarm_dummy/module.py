#!/usr/bin/python3
#
# Part of RedELK
#
# Author: Lorenzo Bernardi / @fastlorenzo
#
from modules.helpers import *
import traceback
import config
import logging

info = {
    'version': 0.1,
    'name': 'dummy alarm',
    'alarmmsg': 'ALARM GENERATED BY DUMMY',
    'description': 'This alarm always triggers. Only use for testing purposes.',
    'type': 'redelk_alarm',
    'submodule': 'alarm_dummy'
}

class Module():
    def __init__(self):
        self.logger = logging.getLogger(info['submodule'])
        pass

    def run(self):
        ret = initial_alarm_result
        ret['info'] = info
        ret['fields'] = ['@timestamp', 'host.name', 'user.name', 'ioc.type', 'file.name', 'file.hash.md5', 'ioc.domain', 'c2.message', 'alarm.alarm_filehash']
        ret['groupby'] = []
        self.logger.debug('Running dummy alarm')
        for r in self.alarm_dummy():
            ret['hits']['hits'].append(r)
            ret['mutations'][r['_id']] = {'test':'extra_data'}
            ret['hits']['total'] += 1

        self.logger.info('finished running module. result: %s hits' % ret['hits']['total'])
        self.logger.debug(ret)
        return(ret)

    def alarm_dummy(self):
        q = "c2.log.type:ioc AND NOT tags:ALARMED_*"
        report = {}
        report['alarm'] = False
        report['fname'] = "alarm_check2"
        report['name'] = "Test IOC's against public sources"
        report['description'] = "This check queries public sources given a list of md5 hashes. If a hash was seen we set an alarm\n"
        report['query'] = q
        iocs = []
        i = countQuery(q, index="rtops-*")
        self.logger.debug('Getting 1 document')
        r = getQuery(q, 100, index="rtops-*")
        self.logger.debug(r)

        return(r)