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
#include <stdio.h>
#include <sys/time.h>

#define PACKETS_NUMBER 10000 // TODO: change to 100000
#define FILE_NAME "syns_result_c"

char *generate_ip_address()
{
    char *ip_address = malloc(16 * sizeof(char));
    srand(time(NULL));
    sprintf(ip_address, "%d.%d.%d.%d", rand() % 256, rand() % 256, rand() % 256, rand() % 256);
    return ip_address;
}

int main()
{
    FILE *fd = fopen(FILE_NAME, "w+");
    struct timeval start, end;

    double sumTime = 0;
    size_t index = 0;
    for (size_t j = 0; j < 100; j++)
    {

        for (size_t i = 0; i < PACKETS_NUMBER ; i++)
        {
            char *ip_address = generate_ip_address();
            char npingCommand[100];
            sprintf(npingCommand, "nping --tcp -c 1 -H -N --quiet --source-ip %s --seq %ld 10.0.0.8", ip_address, index);

            gettimeofday(&start, NULL);
            system(npingCommand);
            gettimeofday(&end, NULL);
            double timeDelta = (end.tv_sec - start.tv_sec) * 1000 + (end.tv_usec - start.tv_usec);

            fprintf(fd, "Packet number: %ld time: %f(ms)\n", index, timeDelta);
            sumTime += timeDelta;
            index++;
            free(ip_address);
        }
        printf("Done with %ld\n", index);
    }
    double avg = sumTime / PACKETS_NUMBER;
    fprintf(fd, "\nThe average time to send a syn packet in c is: %f\n", avg);
    fclose(fd);
    return 0;
}
