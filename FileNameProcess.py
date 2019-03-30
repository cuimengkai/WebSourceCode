# -*-coding:utf-8 -*-
from os import path
from os import listdir
from os import rename
import time
import os

out_welcome_cn = "欢迎来到RENAME!!!\n" \
                 "这个脚本可以帮助你重命名某个文件夹下的文件...\n"
in_folder_path_cn = "请输入文件夹路径：\n"
in_str_add_cn = "请输入你想添加的文字：\n"
in_str_del_cn = "请输入你想删除的文字：\n"
in_str_rename_cn = "请输入重命名后的名称（自动添加后缀）：\n"
in_order_rename_cn = "请输入后缀添加的依据（0. 默认 1. 创建时间 2. 修改时间 3. 访问时间）：\n"
in_choose_folder_or_not_cn = "请选择是否要对此路径下的文件夹操作(对于重命名功能，不建议包含文件夹)[Y/N]:\n"
out_input_error_cn = "你的输入有误，请重新输入：\n"
out_result_success_cn = "所有任务成功完成！"
out_thanks_cn = "感谢你的使用，下次见^_^\n"
out_quit_info_cn = "如果你想退出程序，请输入[n/N]\n"
out_amount_fail_cn = "次任务失败\n"
out_no_path_error_cn = "找不到路径\n"
out_error_happen_cn = "有错误出现\n"
in_choose_fun_info_cn = "请选择功能:\n" \
                     "1. 删除某个文件夹下文件名称中的特定文字\n" \
                     "2. 添加特定的文字到某个文件夹下文件名称的前面\n" \
                     "3. 添加特定的文字到某个文件夹下文件名称的后面\n" \
                     "4. 重命名某个文件夹下所有文件\n" \
                     "n/N: 退出程序\n"


def get_all_files_path(dir_path):
    """

    :param dir_path: the path of directory
    :return: a list includes all of the abspath of files in the directory except folder
    """
    all_files = []
    try:
        while True:
            # ch:if you want to operate the folder
            ch = input(in_choose_folder_or_not_cn)
            if ch == "Y" or ch == "y" or ch == "N" or ch == "n":
                break
            else:
                print(out_input_error_cn)

        for file in listdir(dir_path):
            file_path = path.join(dir_path, file)
            if ch == "N" or ch == "n":
                # if it is file,add it to the list
                if path.isfile(file_path):
                    all_files.append(file_path)
            elif ch == "Y" or ch == "y":
                all_files.append(file_path)
    except WindowsError:
        print(out_no_path_error_cn)

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

            rename(file_path, file_name_final)
            return 1
        else:
            print("No \"" + str_to_del + "\" in " + "\"" + file_path + "\"")
            return -1
    except WindowsError:
        print(out_no_path_error_cn)
        return 0


def add_file_name_str_front(file_path, str_to_add):
    """This function is used to add string to the front of file name

    :param file_path: path of file
    :param str_to_add: string to add
    :return: 1:done -1:string exists 0:error
    """

    try:
        file_name_now = path.basename(file_path)
        if str_to_add not in file_name_now:
            # the directory path of file
            file_abspath_no_name = path.dirname(file_path)
            # file's new name = str_to_add + file's name
            file_name_new = str_to_add + file_name_now
            # join path and file's new name
            file_name_final = path.join(file_abspath_no_name, file_name_new)

            rename(file_path, file_name_final)
            return 1
        else:
            print("\"" + str_to_add + "\" has existed in " + "\"" + file_path + "\"")
            return -1
    except WindowsError:
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
        if str_to_add not in file_name_now:
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

            rename(file_path, file_name_final)
            return 1
        else:
            print("\"" + str_to_add + "\" has existed in " + "\"" + file_path + "\"")
            return -1
    except WindowsError:
        print(out_no_path_error_cn)
        return 0


def folder_file_rename(folder_path, str_rename, order=0):
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
            serial_num_convert = "(" + str(serial_num) + ")"
            file_name_new = file_abspath_no_name + str_rename + serial_num_convert + file_type
            rename(file_path, file_name_new)
            serial_num = serial_num + 1
            count = count + 1
        return count
    except WindowsError:
        print(out_error_happen_cn)


def report_result(total_amount=0, success_amount=0):
    """

    :param total_amount: the number of times a program has been run
    :param success_amount: the number of times that success
    :return: None
    """
    print("It was done " + str(total_amount) + " times missions")
    if total_amount == success_amount and not total_amount == 0:
        print(out_result_success_cn)
    else:
        print(total_amount - success_amount, end="")
        print(out_amount_fail_cn)


def main_process(select):
    """

    :param select: to choose the function
    :return: 1:select can be matched -1:can not identify select
    """
    if select == "1":
        count = 0    # the number of loop
        count_s = 0  # the number of success
        folder_path_input = input(in_folder_path_cn)
        str_to_del_input = input(in_str_del_cn)
        for file_path_tmp in get_all_files_path(folder_path_input):
            count = count + 1
            is_success = del_file_name_str(file_path_tmp, str_to_del_input)
            if is_success == 1:
                count_s = count_s + 1

        report_result(count, count_s)
        return 1

    elif select == "2":
        count = 0  # the number of loop
        count_s = 0  # the number of success
        folder_path_input = input(in_folder_path_cn)
        str_to_add_input = input(in_str_add_cn)
        for file_path_tmp in get_all_files_path(folder_path_input):
            count = count + 1
            is_success = add_file_name_str_front(file_path_tmp, str_to_add_input)
            if is_success == 1:
                count_s = count_s + 1
        report_result(count, count_s)
        return 1

    elif select == "3":
        count = 0  # the number of loop
        count_s = 0  # the number of success
        folder_path_input = input(in_folder_path_cn)
        str_to_add_input = input(in_str_add_cn)
        for file_path_tmp in get_all_files_path(folder_path_input):
            count = count + 1
            is_success = add_file_name_str_behind(file_path_tmp, str_to_add_input)
            if is_success == 1:
                count_s = count_s + 1
        report_result(count, count_s)
        return 1

    elif select == "4":
        folder_path_input = input(in_folder_path_cn)
        str_to_rename_input = input(in_str_rename_cn)
        order = int(input(in_order_rename_cn))
        count = folder_file_rename(folder_path_input, str_to_rename_input, order)
        report_result(count, count)
        return 1
    elif select == "quit" or select == "exit":
        exit(0)

    else:
        print(out_input_error_en)
        print(out_quit_info_en)
        return 0


if __name__ == '__main__':
    print(out_welcome_cn)

    while True:
        key = input(in_choose_fun_info_cn)
        if key == "n" or key == "N":
            print(out_thanks_cn)
            time.sleep(1)
            break

        if main_process(key) == 1:
            print(out_quit_info_cn)
