mysqldump -uroot -p  --default-character-set=utf8 i18n_lab > i18n_lab.sql
mysqldump -uroot -p  --default-character-set=utf8 --no-create-info i18n_lab > i18n_lab_data.sql
CREATE DATABASE i18n_lab CHARACTER SET utf8 COLLATE utf8_bin;