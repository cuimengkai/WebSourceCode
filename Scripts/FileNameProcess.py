# -*-coding:utf-8 -*-
from os import path
from os import listdir
from os import rename
import os
import time

out_welcome_cn = "欢迎来到RENAME!!!\n" \
                 "这个脚本可以帮助你重命名某个文件夹下的文件...\n" \
                 "重命名命令不可撤销！请自行确认后再使用！\n" \
                 "\n" \
                 "Author: Aengus Sun | Blog: www.aengus.top\n" \
                 "-----------------------------------------"
in_folder_path_cn = "请输入文件夹路径（输入数字则默认为当前脚本所在目录）：\n"
in_str_add_cn = "请输入你想添加的文字：\n"
in_str_del_cn = "请输入你想删除的文字：\n"
in_str_rename_cn = "请输入重命名后的名称（自动添加后缀）：\n"
in_order_rename_input_cn = "请输入后缀添加的依据（0. 默认 1. 创建时间 2. 修改时间 3. 访问时间）：\n"
in_order_rename_time_cn = "请输入重命名规则（1. 创建时间 2. 修改时间 3. 访问时间）：\n"
in_str_to_replace_cn = "请输入需要被替换掉的文字：\n"
in_str_new_cn = "请输入新的文字：\n"
in_rule_cn = "请输入重命名的规则（“#”代表重命名后的数字，如输入：新的文件名-# 结果：新的文件名-1、新的文件名-2、...）:\n"
out_input_error_cn = "你的输入有误，请重新输入："
out_total_missions_times_cn = "一共进行了%d次任务"
out_no_str_exist_cn = "文字 \"%s\" 在文件 \"%s\" 名称中不存在！"
out_result_success_cn = "所有任务成功完成！\n"
out_thanks_cn = "感谢你的使用，下次见^_^"
out_quit_info_cn = "如果你想退出程序，请输入[n/N]"
out_amount_fail_cn = "%d次任务失败"
out_mission_compete_cn = "%s 已重命名为 %s"
out_no_path_error_cn = "找不到路径\n" \
                       "请确保输入的路径正确！"
out_error_happen_cn = "有错误出现"
out_same_name_error_cn = "\"%s\" 已存在同名文件！"
out_current_path_cn = "当前工作路径为[ %s ]"
in_choose_fun_info_cn = "请选择功能:\n" \
                     "1. 删除某个文件夹下文件名称中的特定文字\n" \
                     "2. 添加特定的文字到某个文件夹下文件名称的前面\n" \
                     "3. 添加特定的文字到某个文件夹下文件名称的后面\n" \
                     "4. 用输入的文字重命名某个文件夹下所有文件（格式：输入文字(n)，n=1,2,3,...）\n" \
                     "5. 用新的文字替换掉某个文件夹下的特定文字\n" \
                     "6. 用文件的创建/修改/访问时间重命名某个文件夹下的所有文件（格式：年月日-时分秒）\n" \
                     "n/N: 退出程序\n"
# current path
CURRENT_DIR = os.getcwd()
# the path of script
SCRIPT_PATH = path.realpath(__file__)


def get_all_files_path(dir_path):
    """

    :param dir_path: the path of directory
    :return: a list includes all of the abspath of files in the directory except folder
    """
    all_files = []
        try:
        if path.isfile(dir_path):
            all_files.append(dir_path)
            return all_files
        while True:
            # ch: rename folder or not 
            ch = input(in_choose_folder_or_not_cn)
            if ch == "Y" or ch == "y":
                for file_name in listdir(dir_path):
                    file_path = path.join(dir_path, file_name)
                    all_files.append(file_path)
                break
            elif ch == "N" or ch == "n":
                for file_name in listdir(dir_path):
                    file_path = path.join(dir_path, file_name)
                    # if it is file,add it to the list
                    if path.isfile(file_path):
                        all_files.append(file_path)
                break
            else:
                print(out_input_error_cn)

    except OSError:
        print(out_no_path_error_cn)
    if SCRIPT_PATH in all_files:
        all_files.remove(SCRIPT_PATH)
    return all_files

def del_file_name_str(file_path, str_to_del):
    """

    :param file_path: the path of file
    :param str_to_del: the string need to delete
    :return: 1:done -1:no string in name 0:error
    """
    try:
        # the name of file now
        file_name_now = path.basename(file_path)
        if str_to_del in file_name_now:
            # save the path(without name) and type of file
            file_abspath_no_name = path.dirname(file_path)
            # os.path.splitext("E:\\abc.txt")  ---->   tuple("E:\\abc", ".txt")
            file_type = path.splitext(file_path)[1]

            # remove the file-type from file's name
            file_name_deleted_type = file_name_now.replace(file_type, "")

            # the new name(deleted str_to_del) of file without type
            file_name_new_no_type = file_name_deleted_type.replace(str_to_del, "")

            # add the type and path to file
            file_name_new = file_name_new_no_type + file_type
            file_name_final = path.join(file_abspath_no_name, file_name_new)

            try:
                rename(file_path, file_name_final)
                print(out_mission_compete_cn % (file_name_now, file_name_new))
                return 1
            except OSError:
                print(out_same_name_error_cn % file_name_now)
                return 0
        else:
            print(out_no_str_exist_cn % (str_to_del, file_name_now))
            return -1
    except OSError:
        print(out_no_path_error_cn)
        return 0


def add_file_name_str_front(file_path, str_to_add):
    """This function is used to add string to the front of file name

    :param file_path: path of file
    :param str_to_add: string to add
    :return: 1:done  0:error
    """

    try:
        file_name_now = path.basename(file_path)
        # the directory path of file
        file_abspath_no_name = path.dirname(file_path)
        # file's new name = str_to_add + file's name
        file_name_new = str_to_add + file_name_now
        # join path and file's new name
        file_name_final = path.join(file_abspath_no_name, file_name_new)

        try:
            rename(file_path, file_name_final)
            print(out_mission_compete_cn % (file_name_now, file_name_new))
            return 1
        except OSError:
            print(out_same_name_error_cn % file_name_now)
            return 0
    except OSError:
        print(out_no_path_error_cn)
        return 0


def add_file_name_str_behind(file_path, str_to_add):
    """This function is used to add string to the back of file name

    :param file_path: the path of file
    :param str_to_add: the string need to add to the name at the back
    :return: 1:done -1:string exists 0:error
    """
    try:
        file_name_now = path.basename(file_path)
        # the directory path of file
        file_abspath_no_name = path.dirname(file_path)
        # file's type
        file_type = path.splitext(file_path)[1]
        # file's name without type
        file_name_deleted_type = file_name_now.replace(file_type, "")
        # file's new name = file's name + str_to_add
        file_name_new = file_name_deleted_type + str_to_add + file_type
        # join the path and name with type
        file_name_final = path.join(file_abspath_no_name, file_name_new)

        try:
            rename(file_path, file_name_final)
            print(out_mission_compete_cn % (file_name_now, file_name_new))
            return 1
        except OSError:
            print(out_same_name_error_cn % file_name_now)
            return 0
    except OSError:
        print(out_no_path_error_cn)
        return 0


def rename_file_by_input(folder_path, str_rename, order=0):
    """This function can rename all the files in folder and give them a serial number.
    order = 0:The order of the serial number depends on the order of the files in explorer;
    order = 1:The order of the serial number depends on the create time of the files;
    order = 2:The order of the serial number depends on the modify time of the files;
    order = 3:The order of the serial number depends on the assess time of the files.

    :param folder_path: the path of folder
    :param str_rename: the common name of file
    :param order: the flag about order of the serial number
    :return: the number of files
    """
    try:
        serial_num = 1  # serial number
        count = 0
        if order == 0:  # the order of the files in explorer
            list_ordered = get_all_files_path(folder_path)
        elif order == 1:  # the create time of the files
            list_ordered = sorted(get_all_files_path(folder_path), key=lambda file_p: path.getctime(file_p))
        elif order == 2:  # the recent modify time of the files
            list_ordered = sorted(get_all_files_path(folder_path), key=lambda file_p: path.getmtime(file_p))
        elif order == 3:  # the recent assess time of the files
            list_ordered = sorted(get_all_files_path(folder_path), key=lambda file_p: path.getatime(file_p))
        else:
            list_ordered = get_all_files_path(folder_path)

        for file_path in list_ordered:
            # for security，do not use "folder_path"
            # because if the path user input doesn't end with "/",the error will happen
            file_abspath_no_name = path.dirname(file_path) + "/"
            file_type = path.splitext(file_path)[1]
            file_name_now = path.basename(file_path)
            serial_num_convert = "(" + str(serial_num) + ")"
            file_name_new = str_rename + serial_num_convert + file_type
            file_name_final = path.join(file_abspath_no_name, file_name_new)
            try:
                rename(file_path, file_name_final)
                print(out_mission_compete_cn % (file_name_now, file_name_new))
            except OSError:
                print(out_same_name_error_cn % path.basename(file_path))
            serial_num = serial_num + 1
            count = count + 1
        return count
    except OSError:
        print(out_error_happen_cn)


def file_name_replace(file_path, str_to_replace, str_new):
    """

    :param file_path: the path of file
    :param str_to_replace: the string to be replaced in the name of file
    :param str_new: the new string which replace the str_to_replace
    :return: 1: done -1: no string in name 0: error
    """
    try:
        file_name_now = path.basename(file_path)
        if str_to_replace in file_name_now:
            file_abspath_no_name = path.dirname(file_path)
            file_type = path.splitext(file_path)[1]
            file_name_no_type = file_name_now.replace(file_type, "")
            file_name_new = file_name_no_type.replace(str_to_replace, str_new)+file_type
            file_name_final = path.join(file_abspath_no_name, file_name_new)

            try:
                rename(file_path, file_name_final)
                print(out_mission_compete_cn % (file_name_now, file_name_new))
                return 1
            except OSError:
                print(out_same_name_error_cn)
                return 0
        else:
            print(out_no_str_exist_cn % (str_to_replace, file_name_now))
            return -1
    except OSError:
        print(out_no_path_error_cn)
        return 0


def rename_file_by_time_accurate(file_path, order=0):
    """
    like function@rename_file_by_time()
    format: YearMonthDay-HourMinuteSecond

    if you want to use this function, please modify the code of main_process():

    if select == "6":
        folder_path_input = input_path_and_check()
        order = int(input(in_order_rename_time_cn))
        for file_path in get_all_files_path(folder_path_input, order)
            is_success = rename_file_by_time(folder_path_input, order)
            if is_success == 1:
                count_s += 1
            count += 1
        report_result(count, count_s)
        return 1

    :param file_path: file path
    :param order: 2: modify time  3: assess time other: create time
    :return: 1:success 0: path error -1: same name file exists
    """
    try:
        file_type = path.splitext(file_path)[1]
        # get a float
        if order == 2:
            file_time = path.getmtime(file_path)
        elif order == 3:
            file_time = path.getatime(file_path)
        else:
            file_time = path.getctime(file_path)
        # format the time
        # time.localtime(time): getctime()->localtime
        file_time_format = time.strftime("%Y%m%d-%H%M%S", time.localtime(file_time))
        file_name_new = str(file_time_format) + file_type
        file_name_final = path.join(path.dirname(file_path), file_name_new)
        try:
            rename(file_path, file_name_final)
            print(out_mission_compete_cn % (path.basename(file_path), file_name_new))
            return 1
        except OSError:
            print(out_same_name_error_cn)
            return -1

    except OSError:
        print(out_no_path_error_cn)
        return 0


def rename_file_by_time(folder_path, order):
    """
    rename file by create/modify/assess time
    format: YearMonthDay-1/2/3/...
    order = 2: modify time
    order = 3: assess time
    order = others: create time
    :param folder_path: the folder of path
    :param order: the order
    :return: the amount of files
    """
    try:
        serial_num = 1  # serial number
        count = 0
        if order == 2:  # the recent modify time of the files
            list_ordered = sorted(get_all_files_path(folder_path), key=lambda file_p: path.getmtime(file_p))
        elif order == 3:  # the recent assess time of the files
            list_ordered = sorted(get_all_files_path(folder_path), key=lambda file_p: path.getatime(file_p))
        else:
            list_ordered = sorted(get_all_files_path(folder_path), key=lambda file_p: path.getctime(file_p))

        for file_path in list_ordered:
            file_type = path.splitext(file_path)[1]
            # get a float
            if order == 2:
                file_time = path.getmtime(file_path)
            elif order == 3:
                file_time = path.getatime(file_path)
            else:
                file_time = path.getctime(file_path)
            # format the time
            # time.localtime(time): getctime()->localtime
            file_time_format = time.strftime("%Y%m%d-", time.localtime(file_time))
            file_name_new = str(file_time_format) + str(serial_num) + file_type
            file_name_final = path.join(path.dirname(file_path), file_name_new)
            try:
                rename(file_path, file_name_final)
            except OSError:
                print(out_same_name_error_cn)
            print(out_mission_compete_cn % (path.basename(file_path), file_name_new))
            serial_num = serial_num + 1
            count = count + 1
        return count

    except OSError:
        print(out_error_happen_cn)


def rename_file_by_rule(folder_path, rule, order):
    """
    User input the rule of rename then script will rename files by rule, the serial number of file matches "#".
     For example:
     rule: New_name_#
     new name: New_name_1  New_name_2  New_name_3 ....
    :param folder_path: the path of folder
    :param rule: the rule of rename
    :param order: the rule of sort 0: default 1: create 2: modify 3: assess
    :return: the number of files
    """
    try:
        serial_num = 1  # serial number
        count = 0
        if order == 0:  # the order of the files in explorer
            list_ordered = get_all_files_path(folder_path)
        elif order == 1:  # the create time of the files
            list_ordered = sorted(get_all_files_path(folder_path), key=lambda file_p: path.getctime(file_p))
        elif order == 2:  # the recent modify time of the files
            list_ordered = sorted(get_all_files_path(folder_path), key=lambda file_p: path.getmtime(file_p))
        elif order == 3:  # the recent assess time of the files
            list_ordered = sorted(get_all_files_path(folder_path), key=lambda file_p: path.getatime(file_p))
        else:
            list_ordered = get_all_files_path(folder_path)
    
        for file_path in list_ordered:
            # for security，do not use "folder_path"
            # because if the path user input doesn't end with "/",the error will happen
            file_abspath_no_name = path.dirname(file_path) + "/"
            file_type = path.splitext(file_path)[1]
            file_name_new = rule.replace("#", str(serial_num)) + file_type
            file_name_final = path.join(file_abspath_no_name, file_name_new)
            try:
                rename(file_path, file_name_final)
            except OSError:
                print(out_same_name_error_cn)
            print(out_mission_compete_cn % (path.basename(file_path), file_name_new))
            serial_num += 1
            count += 1
        return count

    except OSError:
        print(out_error_happen_cn)
        
        
def report_result(total_amount=0, success_amount=0):
    """

    :param total_amount: the number of times a program has been run
    :param success_amount: the number of times that success
    :return: None
    """
    print(out_total_missions_times_cn % total_amount)
    if total_amount == success_amount and not total_amount == 0:
        print(out_result_success_cn)
    else:
        print(out_amount_fail_cn % (total_amount-success_amount))
    print("-------------------------\n")


def input_path_and_check():
    """

    :return: right folder path
    """
    while True:
        folder_path_input = input(in_folder_path_cn)
        # If user input a number,return the current folder path
        if folder_path_input.isdigit():
            return CURRENT_DIR

        if path.isdir(folder_path_input):
            return folder_path_input
        else:
            print(out_no_path_error_cn)


def main_process(select):
    """

    :param select: to choose the function
    :return: 1:select can be matched -1:can not identify select
    """

    count = 0  # the number of loop
    count_s = 0  # the number of success
    if select == "1":
        folder_path_input = input_path_and_check()
        str_to_del_input = input(in_str_del_cn)
        for file_path_tmp in get_all_files_path(folder_path_input):
            count = count + 1
            is_success = del_file_name_str(file_path_tmp, str_to_del_input)
            if is_success == 1:
                count_s = count_s + 1

        report_result(count, count_s)
        return 1

    elif select == "2":
        folder_path_input = input_path_and_check()
        str_to_add_input = input(in_str_add_cn)
        for file_path_tmp in get_all_files_path(folder_path_input):
            count = count + 1
            is_success = add_file_name_str_front(file_path_tmp, str_to_add_input)
            if is_success == 1:
                count_s = count_s + 1
        report_result(count, count_s)
        return 1

    elif select == "3":
        folder_path_input = input_path_and_check()
        str_to_add_input = input(in_str_add_cn)
        for file_path_tmp in get_all_files_path(folder_path_input):
            count = count + 1
            is_success = add_file_name_str_behind(file_path_tmp, str_to_add_input)
            if is_success == 1:
                count_s = count_s + 1
        report_result(count, count_s)
        return 1

    elif select == "4":
        folder_path_input = input_path_and_check()
        str_to_rename_input = input(in_str_rename_cn)
        order = int(input(in_order_rename_input_cn))
        count = rename_file_by_input(folder_path_input, str_to_rename_input, order)
        report_result(count, count)
        return 1

    elif select == "5":
        folder_path_input = input_path_and_check()
        str_to_replace_input = input(in_str_to_replace_cn)
        str_new_input = input(in_str_new_cn)
        for file_path_tmp in get_all_files_path(folder_path_input):
            count += 1
            is_success = file_name_replace(file_path_tmp, str_to_replace_input, str_new_input)
            if is_success == 1:
                count_s += 1
        report_result(count, count_s)
        return 1

    elif select == "6":
        folder_path_input = input_path_and_check()
        order = int(input(in_order_rename_time_cn))
        count = rename_file_by_time(folder_path_input, order)
        report_result(count, count)
        return 1

    elif select == "7":
        folder_path_input = input_path_and_check()
        order = int(input(in_order_rename_input_cn))
        rule = input(in_rule_cn)
        count = rename_file_by_rule(folder_path_input, rule, order)
        report_result(count, count)
        return 1
    
    elif select == "quit" or select == "exit":
        exit(0)

    else:
        print(out_input_error_cn)
        print(out_quit_info_cn)
        print("---------------------------------\n")
        return 0


if __name__ == '__main__':
    print(out_welcome_cn)
    print(out_current_path_cn % CURRENT_DIR)

    while True:
        choose = input(in_choose_fun_info_cn)
        if choose == "n" or choose == "N":
            print(out_thanks_cn)
            time.sleep(1)
            break
        else:
            main_process(choose)


