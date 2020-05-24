section	.text
			global	ft_strlen

ft_strlen:
			xor rax, rax
			jmp	zerocomp
up:
			inc	rax
zerocomp:
			cmp	BYTE [rdi + rax], 0
			jnz	up
finish:
			ret							