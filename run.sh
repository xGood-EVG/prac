#!/bin/bash
# запускать из корневой директории вашего гит-репозитория
HIM="Леухин Илья" # имя вашего партнёра с http://grep.cs.msu.ru/prac/
BASE_DIR=$(pwd)
find "$BASE_DIR" -type d -name "check" | grep "2024" | while read -r CHECK_DIR; do
    FILE_PATH="$CHECK_DIR/remote"
    RELATIVE_PATH=$(realpath --relative-to="$BASE_DIR" "$CHECK_DIR" | sed 's|/check$||')
    cat << EOF > "$FILE_PATH"
[remote]
"$HIM:$RELATIVE_PATH/1" = []
"$HIM:$RELATIVE_PATH/2" = []
"$HIM:$RELATIVE_PATH/3" = []
EOF

echo "Файл создан: $FILE_PATH"
done
