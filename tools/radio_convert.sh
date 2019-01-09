#! /bin/bash

BASE_DIR=$(pwd)

# _exit() {
# }
# trap _exit EXIT

too_long() {
  for file in "$BASE_DIR"/*; do
    if [[ "$file" = *".mp4" ]] || [[ "$file" = *".webm" ]] || [[ "$file" = *".mkv" ]]; then
      local filename=$(echo "$file" | cut -d'.' -f 1)
      
      ## Trim 30 min and convert to mp3. 
      ffmpeg -i "$file" -ss 0 -t 1800 "$filename".mp3
    fi
  done
}

to_mp3() {
  for file in "$BASE_DIR"/*; do
    if [[ "$file" = *".mp4" ]] || [[ "$file" = *".webm" ]] || [[ "$file" = *".mkv" ]]; then
      local filename=$(echo "$file" | cut -d'.' -f 1)
      ffmpeg -i "$file" "$filename".mp3
    fi
  done
}


main() {
  if (( "$#" != 1 )); then
    echo "Need 1 argument."
    exit
  fi

  if [[ "$1" = "conv" ]]; then
    to_mp3
  elif [[ "$1" = "too_long" ]]; then
    too_long
  fi

  mkdir original_files
  mv "$BASE_DIR"/*.mp4 original_files
  mv "$BASE_DIR"/*.webm original_files
  mv "$BASE_DIR"/*.mkv original_files
}

main "$@"
