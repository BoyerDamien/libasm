extern malloc
extern ft_strlen
extern ft_strcpy

section	.text
			global	ft_strdup

ft_strdup:

_get_len:
    call    ft_strlen
    inc     rax
    push    rdi
    mov     rdi, rax

_do_malloc:
    call    malloc
    cmp     rax, 0
    jz      _malloc_error

_copy:
    pop     rdi
	mov		rsi, rdi
	mov		rdi, rax
	call	ft_strcpy

finish:
	ret

_malloc_error:
    mov rax, 0
    ret