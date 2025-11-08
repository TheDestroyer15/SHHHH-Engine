#pragma once
#include <src/util/util.h>


namespace Maple
{
  class Window{
    private:
        short width;
        short height;
        const char* title;
    public:

        Window(short, short, const char*);
        ~Window();

        int Init();

        void Update();
        void Draw();
        void Shutdown();

  };
};