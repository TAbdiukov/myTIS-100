; Orig: https://gist.github.com/Jcpetrucci/55b0fa27adb736c6d20f

DetectHiddenWindows on
DetectHiddenText on
;SetTitleMatchMode 2
;SetTitleMatchMode Slow


SoundBeep, 750, 100
SetKeyDelay 50

numpadDot::
	SoundBeep, 750, 100
	Sleep 2000 ; allow to change mind
	
	Loop, read, .\dict.txt
	{
		TrayTip Try:, %A_LoopReadLine%, 1 ;Creates tooltip so we can monitor the progress through wordlist.
		
		; Len := StrLen(%A_LoopReadLine%)

		Loop, 5
		{
			Send, {BACKSPACE}1
		}
		
		SendRaw %A_LoopReadLine% ;Type the current line into box
		send ^{f5} ;Submit this password
		
		sleep 0.2
		Send, {ESC}
		Send {LCtrl Right} ; enter input mode
	}
	return

