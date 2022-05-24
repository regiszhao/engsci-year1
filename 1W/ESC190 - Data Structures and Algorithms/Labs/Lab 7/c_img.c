#include "c_img.h"
#include <stdio.h>
#include <math.h>

#define MIN(x, y)   ((x) <= (y) ? (x) : (y))

void create_img(struct rgb_img **im, size_t height, size_t width){
    *im = (struct rgb_img *)malloc(sizeof(struct rgb_img));
    (*im)->height = height;
    (*im)->width = width;
    (*im)->raster = (uint8_t *)malloc(3 * height * width);
}


int read_2bytes(FILE *fp){
    uint8_t bytes[2];
    fread(bytes, sizeof(uint8_t), 1, fp);
    fread(bytes+1, sizeof(uint8_t), 1, fp);
    return (  ((int)bytes[0]) << 8)  + (int)bytes[1];
}

void write_2bytes(FILE *fp, int num){
    uint8_t bytes[2];
    bytes[0] = (uint8_t)((num & 0XFFFF) >> 8);
    bytes[1] = (uint8_t)(num & 0XFF);
    fwrite(bytes, 1, 1, fp);
    fwrite(bytes+1, 1, 1, fp);
}

void read_in_img(struct rgb_img **im, char *filename){
    FILE *fp = fopen(filename, "rb");
    size_t height = read_2bytes(fp);
    size_t width = read_2bytes(fp);
    create_img(im, height, width);
    fread((*im)->raster, 1, 3*width*height, fp);
    fclose(fp);
}

void write_img(struct rgb_img *im, char *filename){
    FILE *fp = fopen(filename, "wb");
    write_2bytes(fp, im->height);
    write_2bytes(fp, im->width);
    fwrite(im->raster, 1, im->height * im->width * 3, fp);
    fclose(fp);
}

uint8_t get_pixel(struct rgb_img *im, int y, int x, int col){
    return im->raster[3 * (y*(im->width) + x) + col];
}

void set_pixel(struct rgb_img *im, int y, int x, int r, int g, int b){
    im->raster[3 * (y*(im->width) + x) + 0] = r;
    im->raster[3 * (y*(im->width) + x) + 1] = g;
    im->raster[3 * (y*(im->width) + x) + 2] = b;
}

void destroy_image(struct rgb_img *im)
{
    free(im->raster);
    free(im);
}


void print_grad(struct rgb_img *grad){
    int height = grad->height;
    int width = grad->width;
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            printf("%d\t", get_pixel(grad, i, j, 0));
        }
    printf("\n");    
    }
}

void change_brightness(struct rgb_img *im, float brightness){
    for (int y=0; y<(im->height); y++){
        for (int x=0; x<(im->width); x++){
            int r = MIN(brightness * get_pixel(im, y, x, 0), 255);
            int g = MIN(brightness * get_pixel(im, y, x, 1), 255);
            int b = MIN(brightness * get_pixel(im, y, x, 2), 255);
            set_pixel(im, y, x, r, g, b);
        }
    }
    return;
}


int main(void){
    
    char *infile = "pic.bin";

    struct rgb_img *img1;
    read_in_img(&img1, infile);
    change_brightness(img1, 0.5);
    write_img(img1, "pic1.bin");

    struct rgb_img *img2;
    read_in_img(&img2, infile);
    change_brightness(img2, 0.75);
    write_img(img2, "pic2.bin");

    struct rgb_img *img3;
    read_in_img(&img3, infile);
    change_brightness(img3, 1.1);
    write_img(img3, "pic3.bin");

    struct rgb_img *img4;
    read_in_img(&img4, infile);
    change_brightness(img4, 1.25);
    write_img(img4, "pic4.bin");

    struct rgb_img *img5;
    read_in_img(&img5, infile);
    change_brightness(img5, 1.5);
    write_img(img5, "pic5.bin");

    return 0;
}