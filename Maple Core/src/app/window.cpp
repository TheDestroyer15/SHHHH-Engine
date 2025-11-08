#include "window.h"

namespace Maple
{
    Window::Window(short width, short height, const char* title)
    {
        this->width = width;
        this->height = height;
        this->title = title;
    }



    
    Window::~Window()
    {
        // Cleanup resources
    }
};
