#include <sys/stat.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <signal.h>
#include <string.h>
#include "stdio.h"
#include "errno.h"
#include "stdlib.h"
#include "unistd.h"
#include <time.h>

char *generate_ip_address()
{
    char *ip_address = malloc(16 * sizeof(char));
    srand(time(NULL));
    sprintf(ip_address, "%d.%d.%d.%d", rand() % 256, rand() % 256, rand() % 256, rand() % 256);
    return ip_address;
}

int main()
{
    char *ip_address = generate_ip_address();
    char npingCommand[100];
    sprintf(npingCommand, "nping --tcp --source-ip %s 10.0.0.8", ip_address);
    printf("%s\n", npingCommand);

    system(npingCommand);

    free(ip_address);
    return 0;
}
