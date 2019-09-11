rename(sela_msg)
{
	sel_msg := sela_msg
	hwnd := WinExist("A")
	WinGetClass class, ahk_id %hwnd%
	if (class="CabinetWClass" or class="ExploreWClass")
	{
		for window in ComObjCreate("Shell.Application").Windows
		{
			if (window.hwnd==hwnd)
			{
				sel :=  window.Document.SelectedItems
				for item in sel
				{
					tmp := item.path
					tmp = "%tmp%"
					sel_msg .= tmp " " 
				}
				Run, pythonw C:\Users\FusionX\PycharmProjects\untitled\Renamer-Hotkeys.py %sel_msg%
			}
		}
	}
}

ControlGetFocus() {
	ControlGetFocus var1, A
	return var1
}

WinGetTitle() {
	WinGetTitle, var1, A
	return var1
}

#If WinActive("ahk_class CabinetWClass") and ControlGetFocus()!="Edit1" and ControlGetFocus()!="Edit2" and (WinGetTitle()=="Downloads")

+l::
	sel_msg := "L "
	rename(sel_msg)
	sel_msg := ""
	return
	
+a::
	sel_msg := "A "
	rename(sel_msg)
	sel_msg := ""
	return

+f::
	sel_msg := "F "
	rename(sel_msg)
	sel_msg := ""
	return

+S::
	sel_msg := "S "
	rename(sel_msg)
	sel_msg := ""
	return

+b::
	sel_msg := "B "
	rename(sel_msg)
	sel_msg := ""
	return
	
+k::
	sel_msg := "K "
	rename(sel_msg)
	sel_msg := ""
	return

+n::
	sel_msg := "N "
	rename(sel_msg)
	sel_msg := ""
	return

+t::
	sel_msg := "T "
	rename(sel_msg)
	sel_msg := ""
	return

+h::
	sel_msg := "H "
	rename(sel_msg)
	sel_msg := ""
	return
	
^+h::
	sel_msg := "H_ "
	rename(sel_msg)
	sel_msg := ""
	return

^+i::
	sel_msg := "I_ "
	rename(sel_msg)
	sel_msg := ""
	return
	
^+s::
	sel_msg := "S_ "
	rename(sel_msg)
	sel_msg := ""
	return

^+n::
	sel_msg := "N_ "
	rename(sel_msg)
	sel_msg := ""
	return

return


