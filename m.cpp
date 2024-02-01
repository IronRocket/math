#include <iostream>
#include <SFML/Graphics.hpp>

#ifdef __linux__

#elif _WIN32
    #include <windows.h>
    class Keyboard{
        private:
            INPUT ip;
            int delay;
        public:
            const int ENTER = 13;
            Keyboard(int delay){
                delay = delay;
                ip.type = INPUT_KEYBOARD;
                ip.ki.wScan = 0; // hardware scan code for key
                ip.ki.time = 0;
                ip.ki.dwExtraInfo = 0;

                ip.ki.dwFlags = 0; // 0 for key pres
            }
            void press(int key){
                ip.ki.dwFlags = 0;
                ip.ki.wVk = key;
                SendInput(1, &ip, sizeof(INPUT));
                Sleep(delay);
                ip.ki.dwFlags = KEYEVENTF_KEYUP;
                SendInput(1, &ip, sizeof(INPUT));
            }
            void write(char s[]){
                for(int i = 0;i<strlen(s);i++){
                    ip.ki.dwFlags = 0;
                    Sleep(delay);
                    ip.ki.wVk = VkKeyScanEx(s[i],GetKeyboardLayout(0));
                    SendInput(1, &ip, sizeof(INPUT));
                    Sleep(delay);
                    ip.ki.dwFlags = KEYEVENTF_KEYUP;
                    SendInput(1, &ip, sizeof(INPUT));
                }
            }
    };
#endif


void handleInput(float &x, float &y){
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::A)){
        x -= 0.01;
    }
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::D)){
        x += 0.01;
    }
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::S)){
        y += 0.01;
    }
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::W)){
        y -= 0.01;
    }
}



int main(){
    sf::RenderWindow win(sf::VideoMode(200, 200), "SFML works!");

    
    sf::CircleShape shape(12.f);
    shape.setFillColor(sf::Color::Green);
    float x = 0;
    float y = 0;
    while (win.isOpen())
    {
        sf::Event event;
        while (win.pollEvent(event))
        {
            switch (event.type)
            {
                // window closed
                case sf::Event::Closed:
                    win.close();
                    break;

                // we don't process other types of events
                default:
                    break;
            }
        }
        handleInput(x,y);
        shape.setPosition(sf::Vector2f(x,y));

        win.clear();
        win.draw(shape);
        win.display();
    }

    return 0;
}