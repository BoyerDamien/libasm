section .text
    global ft_strcmp

ft_strcmp:
		xor             rax, rax

_loop:  mov		        cl, byte [rdi + rax]
		mov		        dl, byte [rsi + rax]
        inc             rax
		cmp		        cl, 0
		je	        	_end
		cmp		        dl, 0
		je		        _end
		cmp		        cl, dl
    	je		        _loop
		jmp		        _end

_end:   movsx	        rax, cl
    	movsx	        rdx, dl
	    sub		        rax, rdx
	    ret