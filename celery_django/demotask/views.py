from django.shortcuts import render
# -*- coding: utf8 -*-

# Create your views here.


from django.http import JsonResponse
from celery.utils import uuid
from demotask.tasks import TestTask


def whole_task(request):
    """示例
    """
    uniq_id = uuid()
    task_job = TestTask()
    task_obj = task_job.apply_async((1, 2, 3, 4),
                                {
                                    "a": "aa",
                                    "b": "bb"
                                }, queue="deploy_task",
                                countdown=3,
                                task_id=uniq_id
                                )
    print 'method', request.method
    print task_obj.task_id
    print task_obj.ready()

    result = {
        "status": 200,
        "msg": "ok"
    }
    return JsonResponse(result)

