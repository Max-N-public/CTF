.intel_syntax noprefix
	
.global main

main: #inital parameter 0xee = ebp+0x8
	push rbp
	mov	ebp,esp
	
	cmp	DWORD PTR [ebp+0x8],0x4c
	jg 	part_a	#1. true--> go to part A
	cmp	DWORD PTR [ebp+0x8],0x8 
	jne	part_b #4. true --> go to Part B
	mov	eax,DWORD [ebp+0x8]
	add	eax,0x3
	jmp	part_d
part_a:
	cmp	DWORD PTR [ebp+0x8],0x3
	jne	part_c #2. true --> go to part C
	mov	eax,DWORD [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_b:
	mov	eax,DWORD [ebp+0x8] #eax = 0xee
	sub	eax,0x3 #5. eax = 235
	jmp	part_d #FINISH
	cmp	DWORD PTR [ebp+0x8],0x6a #false so contiue
	jne	part_c
	mov	eax,DWORD [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_c:
	mov	eax,DWORD [ebp+0x8] #eax = 0xee
	add	eax,0x3 #3. eax = decimal 241 / F1
part_d:
	pop	rbp
	ret

