.intel_syntax noprefix
.bits 32
	
.global asm0

asm0:
	push	ebp
	mov	ebp,esp

	mov	eax,DWORD PTR [ebp+0x8] #x7a
	mov	ebx,DWORD PTR [ebp+0xc] #xd8
	mov	eax,ebx 
	mov	esp,ebp
	pop	ebp	
	ret
