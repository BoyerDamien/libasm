;All syscall is ASM
; 1 -> sys_exit
; 2 -> sys_fork
; 3 -> sys_read
; 4 -> sys_write
; 5 -> sys_open
; 6 -> sys_close

section	.text
			global	ft_strlen

ft_strlen:
			xor, rax, rax
			jmp	zerocomp

up:
			inc	rax
zerocomp:
			cmp	BYTE [rdi + rax], 0
			jnz	up
finish:
			ret							