.intel_syntax noprefix
.bits 32
	
.global asm2

asm2:
	push   	ebp #useless
	mov    	ebp,esp #useless
	sub    	esp,0x10 #reserve 16 bytes on the stack
	mov    	eax,DWORD PTR [ebp+0xc] #0x28 == eax (32bits)
	mov 	DWORD PTR [ebp-0x4],eax
	mov    	eax,DWORD PTR [ebp+0x8] #0x6 == eax (32bits)
	mov	DWORD PTR [ebp-0x8],eax
	jmp    	part_b
part_a:	
	add    	DWORD PTR [ebp-0x4],0x1
	add	DWORD PTR [ebp+0x8],0x8f
part_b:	
	cmp    	DWORD PTR [ebp+0x8],0x8f90 #useless
	jle    	part_a
	mov    	eax,DWORD PTR [ebp-0x4]
	mov	esp,ebp
	pop	ebp
	ret
