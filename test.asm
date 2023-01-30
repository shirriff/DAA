; Test the behavior of the DAA instruction
; This program runs DAA on the values 00-FF
; It runs with all four combinations of carry flag and aux flag set
;
; nasm -f win32 test.asm
; golink /console /mix test.obj msvcrt.dll kernel32.dll
extern ExitProcess, _printf

section .data
msg:
    db  '%x, daa %x, flags %x', 10, 0 ; output line

section .bss
dummy               resd 1

section .text
Start:
    mov     si, 0000h ; no flags
    call    test
    mov     si, 0001h ; carry flag
    call    test
    mov     si, 0010h ; aux flag
    call    test
    mov     si, 0011h ; aux and carry flags
    call    test

    push    0
    call    ExitProcess

; This is the main test loop
; Before calling DAA, the flags are set with the value passed in through si

test:
    push    ebp ; set up stack frame
    mov     ebp, esp

    mov     edi, 0 ; loop counter
loop:
    mov     eax, edi ; set test to the loop counter
    push    si ; set flags from si
    popf

    daa ; The DAA instruction we're testing

    pushf   ; flags, printf arg
    push    eax ; decimal adjusted number, printf arg
    push    edi ; number, printf arg
    push    msg
    call    _printf
    
    inc     edi ; loop 00-ff
    cmp     edi, 100h
    jne     loop

    mov     esp, ebp
    pop     ebp
    ret
