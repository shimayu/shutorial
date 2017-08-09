BITS 32

_start:
    sub esp, 0x40

    ;; open('keyword2.txt', flags, mode);
    xor eax, eax
    push eax
    push 0x7478742e
    push 0x3264726f
    push 0x7779656b
    ;;mov eax, 1024
    mov eax, 0x5
    mov ebx, esp
    xor ecx, ecx
    xor edx, edx
    int 0x80

    ;;read(fd, buf, 0x20);
    mov ebx, eax
    ;;mov eax, 63
    mov eax, 0x3
    mov ecx, esp
    mov edx, 0x20
    int 0x80

    ;;write(1, buf, len);
    mov edx, eax
    ;;mov eax, 64
    mov eax, 0x4
    mov ebx, 0x1
    int 0x80

exit:
    ;; exit(0);
    ;;mov eax, 93
    mov eax, 1
    mov ebx, 0
    int 0x80

    
