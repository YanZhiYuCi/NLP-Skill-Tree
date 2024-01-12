# -*- coding:utf-8 -*-
import os
import pathlib
import shutil
import zipfile
from typing import List


class Directory:

    @staticmethod
    def dir_is_exists(dirs):
        """
        判断文件或文件夹是否存在
        """
        if not os.path.exists(dirs):
            return False
        else:
            return True

    @staticmethod
    def makedirs(dirs):
        if not os.path.exists(dirs):
            os.makedirs(dirs)

    @staticmethod
    def remove_and_makedirs(dirs):
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        else:
            shutil.rmtree(dirs)
            os.makedirs(dirs)

    @staticmethod
    def get_sub_dirs(dirs):
        temp = os.listdir(dirs)
        return [dirs + "/" + _ for _ in temp]

    @staticmethod
    def get_sub_dirs_name(dirs):
        temp = os.listdir(dirs)
        return temp

    @staticmethod
    def remove_dir(dirs):
        if os.path.exists(dirs):
            shutil.rmtree(dirs)

    @staticmethod
    def remove_file(file):
        if os.path.exists(file):
            os.remove(file)

    @staticmethod
    def copy_files(source, target):
        if not os.path.exists(target):
            shutil.copytree(source, target)

    @staticmethod
    def zip_files(src_dir, zip_name):
        z = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(src_dir):
            fpath = dirpath.replace(src_dir, '')
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
        z.close()

    @staticmethod
    def unzip_files(zip_src, dst_dir):
        r = zipfile.is_zipfile(zip_src)
        if r:
            fz = zipfile.ZipFile(zip_src, 'r')
            for file in fz.namelist():
                fz.extract(file, dst_dir)
        else:
            print('This is not zip')

    @staticmethod
    def get_last_level_name(input_data):
        """
        返回最后一级目录名
        例如 D:\Projects\information-extraction\data\model\entity_extraction\ner_mcy_v1 返回ner_mcy_v1
        D:\Projects\information-extraction\data\model\entity_extraction\ner_mcy_v1/ 返回ner_mcy_v1
        D:\Projects\information-extraction\data\model\entity_extraction\README.txt 返回 README.txt
        :param input_data:
        :return:
        """
        last_level_dir_name = pathlib.PurePath(input_data).name
        return last_level_dir_name

    @staticmethod
    def convert_res_dir_name_from_nlp_task_to_txt_name(temp_dirs):
        dirs = '_'.join(temp_dirs.split('_')[:-1])
        txt_file_name_set = set()
        nlp_task_type_name_list = [per for per in os.listdir(temp_dirs) if per != 'logs']
        for nlp_task_type_name in nlp_task_type_name_list:
            current_nlp_task_type_name_dir = os.path.join(temp_dirs, nlp_task_type_name)
            for txt_file_res_json in os.listdir(current_nlp_task_type_name_dir):
                txt_file_name = txt_file_res_json[:-5]  # 这里默认文件后缀为.json
                txt_file_name_set.add(txt_file_name)
        txt_file_name_list = list(txt_file_name_set)

        Directory.makedirs(dirs)
        for txt_file_name in txt_file_name_list:
            txt_file_name_dir = os.path.join(dirs, txt_file_name)
            Directory.makedirs(txt_file_name_dir)
            for nlp_task_type_name in nlp_task_type_name_list:
                txt_file_name_with_file_format = txt_file_name + '.json'
                source_file_path = os.path.join(temp_dirs, nlp_task_type_name, txt_file_name_with_file_format)
                target_txt_file_name = nlp_task_type_name + '_' + txt_file_name_with_file_format
                target_file_path = os.path.join(txt_file_name_dir, target_txt_file_name)
                if Directory.dir_is_exists(source_file_path):
                    shutil.copy(source_file_path, target_file_path)
        return dirs


    @classmethod
    def get_file_name_and_path(cls, project_root_dir_path, relative_dataset_dir_path, logger):
        dataset_root_dir_path = os.path.join(project_root_dir_path, relative_dataset_dir_path)
        dataset_dir_name: List[str] = os.listdir(dataset_root_dir_path)
        if len(dataset_dir_name) == 0:
            raise Exception('Directory[{}] has no dataset directory.')
        elif len(dataset_dir_name) > 1:
            raise Exception('Directory[{}] has more than one directories.')
        selected_dataset_dir_name = dataset_dir_name[0]
        dataset_dir_path = os.path.join(dataset_root_dir_path, selected_dataset_dir_name)
        logger.info('dataset_dir_path:{}'.format(dataset_dir_path))
        data_file_name: List[str] = os.listdir(dataset_dir_path)
        logger.info('dataset_dir_path[{}] includes files:{}'.format(dataset_dir_path, data_file_name))
        data_file_path = [os.path.join(dataset_dir_path, p) for p in data_file_name]
        return dataset_dir_path, data_file_name, data_file_path


if __name__ == '__main__':
    dirs = r'D:\Projects\information-extraction\data\output_root_for_prediction\all-in-one_1675154799245242'
    Directory.convert_res_dir_name_from_nlp_task_to_txt_name(dirs)
