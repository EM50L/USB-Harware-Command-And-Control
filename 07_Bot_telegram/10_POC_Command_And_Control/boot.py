import usb_cdc, usb_hid, storage, supervisor

#Desabilito acceso a disco. esto sirve para "ocultar el dispositivo"
storage.disable_usb_drive() #desabilito storaje para liberar endpoints

#Configuro parametros USB:         Fabricante    , Producto          , VID  , PID
supervisor.set_usb_identification("Sh3llC0N_2024","Understanding_USB",0x16c0,0x27db)

#Ojo si desabilitas el CDC y storage pierdes el control del dispositivo
#solo podrias acceder desde la interfaz web (falla bastante)
usb_cdc.disable()

#usb_hid.enable((usb_hid.Device.KEYBOARD,usb_hid.Device.MOUSE,USB_hid.Device.CONSUMER_CONTROL))
#usb_hid.enable((usb_hid.Device.KEYBOARD,usb_hid.Device.MOUSE))
usb_hid.enable((usb_hid.Device.KEYBOARD,))

print("fin boot.py")