# -*- coding:UTF-8 -*-
import cv2 as cv
from os import path
from time import sleep
import os

out_welcome_cn = "欢迎来到图片处理脚本！\n" \
                 "此脚本需要安装opencv-python\n" \
                 "请使用pip install opencv-python命令安装\n" \
                 "\n" \
                 "Author: Aengus Sun | Blog: www.aengus.top\n" \
                 "-----------------------------------------"
out_not_image_cn = "：%s 不是图像文件！"
out_no_path_error_cn = "你输入的路径有误！\n" \
                       "请确保输入的路径中没有中文！"
out_source_img_info_cn = "照片[%s]初始的水平方向像素数为[%d]，垂直方向像素数[%d]"
out_destination_img_info_cn = "处理后水平像素数变为[%d]，垂直方向像素数变为[%d]"
out_mission_times_cn = "总共进行了%d次任务"
out_all_success_cn = "所有任务全都完成！\n" \
                     "---------------"
out_fail_times_cn = "一共有%d次任务失败\n" \
                    "-----------------"
out_input_error_cn = "你的输入有误，请重新输入！"
out_thanks_use_cn = "感谢你的使用，下次使用再见^_^"
out_ratio_imbalance_cn = "水印比例与原图比例严重失衡！"
out_mission_complete_cn = "%s 创建完成"
out_current_dir_path_cn = "当前路径为 %s"
input_choose_function = "请选择功能：\n" \
                        "1. 将所有图片的水平像素调整为统一的值\n" \
                        "2. 给所有图片右下角添加水印\n" \
                        "3. 给所有图片中间添加水印\n" \
                        "n/N. 退出脚本\n"
input_folder_path_cn = "请输入图片文件夹路径（输入数字表示当前脚本所在文件夹）：\n"
input_new_size_level = "请输入图片修改后的水平像素数量：\n"
input_choose_folder_or_not_cn = "请选择是否要对此路径下的文件夹操作(对于重命名功能，不建议包含文件夹)[Y/N]:\n"

# 脚本所在目录
CURRENT_DIR = os.getcwd()
# 脚本路径
SCRIPT_PATH = path.realpath(__file__)


def get_all_images(dir_path):
    all_images = []
    # opencv支持的文件类型
    image_type = [".jpg", ".jpeg", ".jpe", ".bmp", ".png", ".dib",
                  ".pbm", ".pgm", ".ppm", ".sr", ".ras", ".tiff", ".tif", ".exr", ".jp2"]
    try:
        # 如果输入的是文件路径
        if path.isfile(dir_path):
            file_type = path.splitext(dir_path)[1]
            if file_type in image_type:
                all_images.append(dir_path)
                return all_images

        for file in os.listdir(dir_path):
            file_path = path.join(dir_path, file)
            if path.isfile(file_path):
                file_type = path.splitext(file_path)[1]
                if file_type in image_type:
                    all_images.append(file_path)
                else:
                    print(out_not_image_cn % path.basename(file_path))

    except OSError:
        print(out_no_path_error_cn)
    if SCRIPT_PATH in all_images:
        all_images.remove(SCRIPT_PATH)
    return all_images


def img_size_reset(image_path, new_size_level, image_dir_path):
    """输入图片的目标水平像素值，生成一个图片：原图片名[目标水平像素值]

    :param image_path: 图片路径
    :param new_size_level: 修改后图片的水平像素数量
    :param image_dir_path: 图片所在文件夹路径，这里是为了减少时间花销
    :return: 1：成功 0：图片路径错误
    """
    try:
        src = cv.imread(image_path)
        try:
            if src.shape[1] == new_size_level:
                return 1
        except AttributeError:
            print(out_no_path_error_cn)
            return 0
    except OSError:
        print(out_no_path_error_cn)
        return 0
    image_name = path.basename(image_path)
    image_type = path.splitext(image_path)[1]
    image_name_no_type = image_name.replace(image_type, "")
    # 修改后
    dst_new_name = image_name_no_type + "[" + str(new_size_level) + "]" + image_type
    dst_abspath = path.join(image_dir_path, dst_new_name)

    # shape[0]: 垂直像素（行数），shape[1]: 水平像素（列数）
    # dst_level：水平方向像素数量，dst_vertical: 垂直方向像素数量
    print(out_source_img_info_cn % (image_name, src.shape[1], src.shape[0]))
    if new_size_level >= src.shape[1]:   # 图片放大
        multiple = new_size_level/src.shape[1]
        dst_vertical, dst_level = int(src.shape[0]*multiple), new_size_level
    else:    # 图片缩小
        multiple = src.shape[1]/new_size_level
        dst_vertical, dst_level = int(src.shape[0]/multiple), new_size_level
    dst = cv.resize(src, (dst_level, dst_vertical))
    print(out_destination_img_info_cn % (dst_level, dst_vertical))
    print(out_mission_complete_cn % dst_new_name)

    cv.imwrite(dst_abspath, dst)
    return 1


def add_watermark_at_low_right(image_path, watermark_path, image_dir_path, ratio=12):
    """
    添加水印到图片的右下角，水印添加位置是按原图像比例距离右下边缘1/6处，水印大小是原图像长度的1/20
    :param image_path: 原图像路径
    :param watermark_path: 水印图像路径
    :param image_dir_path: 图片目录路径
    :param ratio: 原图水平方向像素数量和水印的比例
    :return: 1：成功  0：失败   -1: 水印在将要操作的文件夹中，跳过
    """
    try:
        image_name = path.basename(image_path)
        watermark_name = path.basename(watermark_path)
        if image_name == watermark_name:
            return -1
        src = cv.imread(image_path)
        src_watermark = cv.imread(watermark_path)
    except OSError:
        print(out_no_path_error_cn)
        return 0
    image_type = path.splitext(image_path)[1]
    image_name_no_type = image_name.replace(image_type, "")
    # 修改后的图片路径
    dst_new_name = image_name_no_type + "[lr-watermark]" + image_type
    dst_abspath = path.join(image_dir_path, dst_new_name)

    # 得到与待添加水印图片相同尺寸的掩膜
    dst_watermark = src - src
    # 水印处理
    watermark_ratio = src_watermark.shape[0]/src_watermark.shape[1]  # 水印宽长比
    watermark_length = int(src.shape[1]/ratio)  # 水印长度
    watermark_width = int(watermark_length*watermark_ratio)  # 水印宽度
    watermark = cv.resize(src_watermark, (watermark_length, watermark_width))
    # 将水印添加到掩膜的某个位置
    src_ratio = src.shape[0]/src.shape[1]  # 原图像的宽长比
    watermark_x = src.shape[1] - int(src.shape[1] / 6)
    watermark_y = src.shape[0] - int((src.shape[1] / 6) * src_ratio)
    try:
        dst_watermark[watermark_y:watermark_y+watermark.shape[0],
                      watermark_x:watermark_x+watermark.shape[1]] = watermark
        # 将掩膜与原图像融合（加水印）
        dst = cv.addWeighted(src, 1, dst_watermark, 1, 1)

        cv.imwrite(dst_abspath, dst)
        print(out_mission_complete_cn % dst_new_name)
        return 1
    except ValueError:
        print(out_ratio_imbalance_cn)
        return 0


def add_watermark_at_middle(image_path, watermark_path, image_dir_path, ratio=12):
    """
        添加水印到图片的中间，水印大小是原图像长度的1/20
        :param image_path: 原图像路径
        :param watermark_path: 水印图像路径
        :param image_dir_path: 图片目录路径
        :param ratio: 原图水平像素数量和水印的比例
        :return: 1：成功  0：失败  -1：水印在操作的文件夹中，跳过
        """
    try:
        image_name = path.basename(image_path)
        watermark_name = path.basename(watermark_path)
        if image_name == watermark_name:
            return -1
        src = cv.imread(image_path)
        src_watermark = cv.imread(watermark_path)
    except OSError:
        print(out_no_path_error_cn)
        return 0
    image_name = path.basename(image_path)
    image_type = path.splitext(image_path)[1]
    image_name_no_type = image_name.replace(image_type, "")
    # 修改后的图片路径
    dst_new_name = image_name_no_type + "[mid-watermark]" + image_type
    dst_abspath = path.join(image_dir_path, dst_new_name)

    # 得到与待添加水印图片相同尺寸的掩膜
    dst_watermark = src - src
    try:
        # 水印处理
        watermark_ratio = src_watermark.shape[0] / src_watermark.shape[1]  # 水印宽长比
    except AttributeError:
        print(out_no_path_error_cn)
        return 0
    watermark_length = int(src.shape[1] / ratio)  # 水印长度
    watermark_width = int(watermark_length * watermark_ratio)  # 水印宽度
    watermark = cv.resize(src_watermark, (watermark_length, watermark_width))
    # 将水印添加到掩膜的中间位置
    watermark_x = int(src.shape[1] - src.shape[1] / 2 - watermark_length / 2)
    watermark_y = int(src.shape[0] - src.shape[0] / 2 - watermark_width / 2)
    try:
        dst_watermark[watermark_y:watermark_y + watermark.shape[0],
                      watermark_x:watermark_x + watermark.shape[1]] = watermark
        # 将掩膜与原图像相加（加水印）
        dst = cv.addWeighted(src, 1, dst_watermark, 1, 1)

        cv.imwrite(dst_abspath, dst)
        print(out_mission_complete_cn % dst_new_name)
        return 1
    except ValueError:
        print(out_ratio_imbalance_cn)
        return 0


def input_path_and_check():
    """
    输入路径并检查
    :return: 正确的路径
    """
    while True:
        folder_path_input = input(input_folder_path_cn)
        if folder_path_input.isdigit():
            return CURRENT_DIR
        if path.isdir(folder_path_input):
            return folder_path_input
        else:
            print(out_no_path_error_cn)


def main_process(select):
    count = 0
    count_s = 0
    if select == "1":  # 调整图片水平像素值
        folder_path_input = input_path_and_check()
        new_size_level = int(input(input_new_size_level))
        for img_path in get_all_images(folder_path_input):
            is_success = img_size_reset(img_path, new_size_level, folder_path_input)
            count += 1
            if is_success == 1:
                count_s += 1
        result_report(count, count_s)
        return 1

    elif select == "2":  # 给所有图片右下角添加水印
        folder_path_input = input_path_and_check()
        watermark_path_input = input("请输入水印图片路径：\n")
        for image_path in get_all_images(folder_path_input):
            is_success = add_watermark_at_low_right(image_path, watermark_path_input, folder_path_input)
            count += 1
            if is_success == 1:
                count_s += 1
            if is_success == -1:
                count -= 1
        result_report(count, count_s)
        return 1

    elif select == "3":  # 给所有图片中间添加水印
        folder_path_input = input_path_and_check()
        watermark_path_input = input("请输入水印图片路径：\n")
        for image_path in get_all_images(folder_path_input):
            is_success = add_watermark_at_middle(image_path, watermark_path_input, folder_path_input)
            count += 1
            if is_success == 1:
                count_s += 1
            if is_success == -1:
                count -= 1
        result_report(count, count_s)
        return 1

    else:
        print(out_input_error_cn)


def result_report(total_times, success_times):
    print(out_mission_times_cn % total_times)
    if total_times == success_times and not total_times == 0:
        print(out_all_success_cn)
    else:
        print(out_fail_times_cn % int(total_times - success_times))


if __name__ == "__main__":
    print(out_welcome_cn)
    print(out_current_dir_path_cn % CURRENT_DIR)

    while True:
        choose = input(input_choose_function)
        if choose == "n" or choose == "N":
            print(out_thanks_use_cn)
            sleep(1)
            break
        main_process(choose)

