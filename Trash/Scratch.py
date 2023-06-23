if fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[
                        4] == 0:

                        while t:
                            os.startfile("C:\Program Files\Microsoft Office\\root\Office16\WINWORD.EXE")
                            os.system("C:\Program Files\Microsoft Office\\root\Office16\WINWORD.EXE")
                            t = False
                        # for ctrlz(cut)
                    # 2
                    elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[
                        4] == 0 and length2 < 40:

                        while t:
                            pyautogui.hotkey('ctrlleft', 'x')
                            t = False

                    # 4
                    elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:

                        while t:
                            pyautogui.hotkey('ctrlleft', 'a')
                            t = False
                    # 5
                    elif fingers[1] == 1 and fingers[0] == 0 and fingers[2] == 1 and fingers[3] == 1 and fingers[
                        4] == 1:

                        while t:
                            pyautogui.hotkey('ctrlleft', 'v')
                            t = False
                        # for altf4(closing)
                    # 6
                    elif fingers[1] == 0 and fingers[0] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[
                        4] == 0:

                        while t:
                            pyautogui.hotkey('altleft', 'F4')
                            t = False

                    # 7
                    elif fingers[1] == 1 and fingers[0] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[
                        4] == 0 :

                        while t:
                            # pyautogui.hotkey('altleft', 'F4')
                            pyautogui.hotkey('win', 'l')
                            t = False

                    # 08
                    elif fingers[1] == 0 and fingers[0] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[
                        4] == 1 and length < 30:

                        while t:
                            pyautogui.hotkey('ctrlleft', 's')
                            t = False
                        # for altf4(closing)
                    # 09
                    elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[
                        4] == 1:

                        while t:
                            pyautogui.hotkey('ctrlleft', 'z')
                            t = False

                    # 10
                    elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[
                        4] == 1:

                        while t:
                            pyautogui.hotkey('ctrlleft', 'p')
                            t = False

                    # 11
                    elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[
                        4] == 0 and length3 > 50:

                        while t:
                            pyautogui.hotkey('ctrlleft', 'b')
                            t = False
                        # for altf4(closing)
                    # 12
                    elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[
                        4] == 1 and length5 < 20:

                        while t:
                            pyautogui.hotkey('ctrlleft', 'i')
                            t = False
                        # for altf4(closing)
                    # 13
                    elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[
                        4] == 1 and length3 < 70:

                        while t:
                            pyautogui.hotkey('ctrlleft', 'u')
                            t = False
                        # for altf4(closing)
                    # 14
                    elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[
                        4] == 0:

                        while t:
                            pyautogui.hotkey('ctrlleft', 'n')
                            t = False
                        # for altf4(closing)
                    # 15
                    if fingers[1] == 0 and fingers[0] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
                        t = False