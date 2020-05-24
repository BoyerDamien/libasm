section .text
    global ft_read

ft_read:
    cmp edi, 0
    jl _error
    cmp rdx, 0
    jl _error
    cmp rsi, 0
    jle _error

_write:
    mov rax, 0
    syscall
    cmp rax, 0
    jl _error
    mov rax, rdx
    ret

_error:
    mov rax, -1
    ret