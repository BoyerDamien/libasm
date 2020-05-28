extern __errno_location
section .text
    global ft_read

ft_read:
        cmp     rdi, 0
        jl      _error
        cmp     rsi, 0
        jle     _error

_read:
        mov     rax, 0
        syscall
        cmp     rax, 0
        jl      _error
        ret

_error:
        neg rax
        mov rcx, rax
        call __errno_location
        mov [rax], rcx
        mov rax, -1 
        ret