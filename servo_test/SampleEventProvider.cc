#include <wiringPi.h>
#include <stdio.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <wiringPi.h>
#include <softServo.h>
#include <unistd.h>
#include <time.h>
#include "acfw/cm/Cm.h"
#include "SampleEvent.h"

#include "acfw/execute/EventBasedRunnable.h"
#include "acfw/log/Logger.h"
#include "acfw/execute/Timer.h"

// #include "services/Twist.h"
// #include "services/Twist.h"
// #include "TinyJson.h"

// #include "Socket_manager.h"
#include <iostream>

using namespace acfw::cm;
using namespace sample;
using namespace std;

static void onState(Service::State state, void* userData)
{
    (void)userData;
    cout << "Provider state changed to: " << (int)state << endl;
}

int main (void)
{
    acfw::cm::initialize();

    const char* spec = R"(
    {
        "class": "event",
        "role": "server",
        "type": "sample::SampleEvent",
        "name": "sample/event",
        "endpoints": [
            {
                "type": "dds",
                "config": {
                    "topic": "sample/event"
                }
            }
        ]
    }
    )";
    // Create service
    SampleEventProvider provider;
    auto r = provider.create(0, spec);
    if (r != Result::OK)
    {
        cout << "Create service provider failed: " << (int)r << endl;
        return 1;
    }
    provider.setStateHandler(onState, &provider);

    // Start service
    r = provider.start();
    if (r != Result::OK)
    {
        cout << "Create service provider failed: " << (int)r << endl;
        return 2;
    }


    if (wiringPiSetup() == -1)  {                   // setup to use Wiring pin numbers
        fprintf(stdout, "oops: %s\n", strerror(errno)) ;
        return 1 ;}

    softServoSetup(1, 12, 24, 22, 4, 5, 6, 7) ;   // wiringPipin numbers
    for (;;)  {
        softServoWrite(1,  0) ; // wiringPipin 0 is BCM_GPIO 17
        softServoWrite(12,  0) ;
        softServoWrite(24,  0) ;
        softServoWrite(22,  0) ;
        delay (1000) ;
        softServoWrite(1,  500) ; // wiringPipin 0 is BCM_GPIO 17
        softServoWrite(12,  500) ;
        softServoWrite(24,  500) ;
        softServoWrite(22,  500) ;
        delay (1000);
        softServoWrite(1,  1000) ; // wiringPipin 0 is BCM_GPIO 17
        softServoWrite(12,  1000) ;
        softServoWrite(24,  1000) ;
        softServoWrite(22,  1000) ;
        delay (1000);}

    acfw::cm::release();
    }