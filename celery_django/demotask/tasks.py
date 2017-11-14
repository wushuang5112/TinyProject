# -*- coding: utf8 -*-

import celery
from json import dumps

class TestTask(celery.Task):
    def run(self, *args, **kwargs):
        print "*" * 80
        print str(args)
        print dumps(kwargs)

        return "--*xx"

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print "*" * 80
        print exc
        print task_id
        print str(args)
        print dumps(kwargs)
        print einfo
        print "*" * 80

    def on_success(self, retval, task_id, args, kwargs):
        print retval
        print task_id
        print str(args)
        print dumps(kwargs)

