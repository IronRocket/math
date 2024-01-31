#include <iostream>
#include <vector>
#include <windows.h>
#include <SFML/Audio.hpp>
#include <SFML/Graphics.hpp>


typedef struct Person{
    int id;
}Person;


class Queue{
    private:
        int id;
        std::vector<Person> v;
    public:
        Queue(int size){
            id = 0;
            Person p = {-1};
            for (int i = 0;i<size-1;i++){
                v.push_back(p);
            }
        }
        int insertPerson(){
            for (int i = 0;i<v.size();i++){
                if(v[i].id == -1){
                    v[i].id = id;
                    id++;
                    return v[i].id;
                }
            }
            return -1;
        }
        int frontPerson(){
            int removedId = v[0].id;
            if (removedId == -1){
                return -1;
            }
            v.erase(v.begin());
            v.insert(v.end(),Person{-1});
            return removedId;
        }
        void printArray(){
            for(int i = 0;i<v.size();i++){
                printf("%d,",v[i].id);
            }
            printf("\n");
        }

};

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

int main(){
    /*
    Keyboard k{50};
    printf("Starting\n");
    while(1){
        if(GetKeyState('R') & 0x8000){
            k.write((char*)"/");
            Sleep(100);
            k.write((char*)"spawn");
            k.press(k.ENTER);
        }
        Sleep(50);
    }
    return 0;*/
    // Create the main window
    sf::RenderWindow window(sf::VideoMode(800, 600), "SFML window");
 
    // Load a sprite to display
    sf::Texture texture;
    if (!texture.loadFromFile("cute_image.jpg"))
        return EXIT_FAILURE;
    sf::Sprite sprite(texture);
 
    // Create a graphical text to display
    sf::Font font;
    if (!font.loadFromFile("arial.ttf"))
        return EXIT_FAILURE;
    sf::Text text("Hello SFML", font, 50);
 
    // Load a music to play
    sf::Music music;
    if (!music.openFromFile("nice_music.ogg"))
        return EXIT_FAILURE;
 
    // Play the music
    music.play();
 
    // Start the game loop
    while (window.isOpen())
    {
        // Process events
        sf::Event event;
        while (window.pollEvent(event))
        {
            // Close window: exit
            if (event.type == sf::Event::Closed){
                window.close();
            }
        }
 
        // Clear screen
        window.clear();
 
        // Draw the sprite
        window.draw(sprite);
 
        // Draw the string
        window.draw(text);
 
        // Update the window
        window.display();
    }
 
    return EXIT_SUCCESS;
}