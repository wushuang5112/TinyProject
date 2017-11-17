def log_analysis(log_text, server_list):
    """日志分析函数
    :param log_text: 日志源
    :param server_list: 服务器列表
    :return: 格式化结果字符串

    [start] 20171117 13:50:45
    [success] 20171117 13:50:45 first step.
    [success] 20171117 13:50:45 second step.
    [error] 20171117 13:50:45 error, ooh, symbol - 2, maybe netword is dump.
    [success] 20171117 13:50:45 do rollback action.
    [success] 20171117 13:50:45 ok, rollback well done.
    [end] 20171117 13:50:45
    """
    if isinstance(server_list, list):
        servers = set(server_list)
    else:
        servers = set(server_list.split(','))
    ip4_reg = "\\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b"
    ip4_pattern = re.compile(ip4_reg)
    server_success = set()

    # 成功日志模块
    success_block = []
    # 失败日志模块
    failed_block = []

    log_text = log_text.splitlines()
    begin_logo = "[start] "
    end_logo = "[end] "
    err_logo = "[error] "
    log_partial = []
    end_status = False
    status = True
    ip_addr = u"0.0.0.0"
    for log in log_text:
        if log.startswith(begin_logo):
            # 用户服务器执行IP
            ip_addr_list = ip4_pattern.findall(log)
            if len(ip_addr_list) == 1:
                ip_addr = servers & set(ip_addr_list)
            else:
                ip_addr = set([u"0.0.0.0"])

            # 开始
            if log_partial:
                log_string = u"\n".join(log_partial)
                if status and end_status:
                    if log_string:
                        success_block.append(log_string)
                    server_success = server_success | ip_addr
                else:
                    if log_string:
                        failed_block.append(log_string)
                # 默认初始状态为
                status = True
                end_status = False

            log_partial = [log]
        elif log.startswith(end_logo):
            # 结束，没有结束标志的认为失败
            end_status = True
            log_partial.append(log)
            if log_partial:
                log_string = u"\n".join(log_partial)
                if status and end_status:
                    if log_string:
                        success_block.append(log_string)
                    server_success = server_success | ip_addr
                else:
                    if log_string:
                        failed_block.append(log_string)
                # 默认初始状态为
                status = True
                end_status = False
            log_partial = []
        else:
            if log.startswith(err_logo):
                status = False
            log_partial.append(log)
    else:
        log_string = u"\n".join(log_partial)
        if end_status:
            if log_string:
                success_block.append(log_string)
            server_success = server_success | ip_addr
        else:
            if log_string:
                failed_block.append(log_string)

    total = len(servers)
    success = len(server_success)

    result = {
        "total": total,         # 总机器数
        "success": success,     # 成功发布机器数
        "s": success_block,     # 成功日志模块
        "f": failed_block,        # 失败日志模块
    }
    return result


if __name__ == "__main__":
    s1 = """/tmp/deploy/deploy_pro.sh: line 2: deploy.lib.sh: No such file or directory
    /tmp/deploy/deploy_pro.sh: line 6: deploy_start: command not found
    /tmp/deploy/deploy_pro.sh: line 8: deploy_success: command not found
    /tmp/deploy/deploy_pro.sh: line 10: deploy_success: command not found
    /tmp/deploy/deploy_pro.sh: line 12: deploy_error: command not found
    /tmp/deploy/deploy_pro.sh: line 14: deploy_success: command not found
    /tmp/deploy/deploy_pro.sh: line 16: deploy_success: command not found
    /tmp/deploy/deploy_pro.sh: line 18: deploy_end: command not found
    """

    s2 = """[start] tag: V1.0 proj: Deploy System env: tst machine: 10.11.12.13
    [info] this is a test log, its show you how to code deploy.
    [success] congratulation!
    [success] all job had done.
    [end] well done.
    """

    s3 = """[start] tag: V1.0 proj: Deploy System env: tst machine: 10.11.12.14
    [info] this is a second log, its show you how to code deploy.
    [success] congratulation!
    [success] all job had done.
    [end] well done.
    """
    s4 = """[start] tag: V1.0 proj: Deploy System env: tst machine: 10.11.12.15
    [info] this is a test log, its show you how to code deploy.
    [success] congratulation!
    [error] but there is a error!
    [end] well done.
    """

    # log = s2 + s3 + s4 + s1

    log = """[start] 20171116 09:49:03
    [success] 20171116 09:49:03 first step.
    [success] 20171116 09:49:03 second step.
    [error] 20171116 09:49:03 error, ooh, maybe netword is dump.
    [success] 20171116 09:49:03 do rollback action.
    [success] 20171116 09:49:03 ok, rollback well done.
    [end] 20171116 09:49:03
    """

    text = log_analysis(log, '10.11.12.13')

    # print text

    from pprint import pprint
    pprint(text)

    print text
