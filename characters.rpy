define gg = Character("[gg_name]", color = "#ff0000", image = 'gg')
define gg_phone = Character("[gg_name]", kind=nvl, callback = Phone_ReceiveSound, color = "#ff0000")

define gmom = Character("Мама", color = "#e600e6", image = 'mom' )

define nvl_nastya = Character(_("Настя"),kind=nvl , color = "#62ffe5ff")
define nastya = Character(_("Настя"), color = "#62ffe5ff",image = 'nastya')
define nastya_phone = Character(_("Настя"), kind=nvl, callback = Phone_ReceiveSound, color = "#62ffe5ff")

define courier = Character(_("Курьер"), color = "#00ca00", image = 'courier')



define beingADick = False