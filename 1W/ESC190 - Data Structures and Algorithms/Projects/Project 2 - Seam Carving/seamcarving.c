#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "c_img.h"
#include "seamcarving.h"

#define DEBUG 0
#define VISUALIZE 0

/****************************************************
 * HELPER FUNCTIONS
 ****************************************************/
void print_pixel(struct rgb_img *im, int y, int x){
    int value;
    for (int i=0; i<3; i++){
        value = get_pixel(im, y, x, i);
        printf("%d ", value);
    }
    return;
}

void print_image(struct rgb_img *im){
    for (int y=0; y<(im->height); y++){
        for (int x=0; x<(im->width); x++){
            print_pixel(im, y, x);
            printf("\t");
        }
        printf("\n");
    }
    return;
}

void print_double_array(double *arr, int height, int width){
    for (int i=0; i<height; i++){
        for (int j=0; j<width; j++){
            printf("%f\t", arr[i*width+j]);
        }
        printf("\n");
    }
}

void print_int_array(int *arr, int height, int width){
    for (int i=0; i<height; i++){
        for (int j=0; j<width; j++){
            printf("%d\t", arr[i*width+j]);
        }
        printf("\n");
    }
}

int array_min(double *arr, int start, int end){
    double min = 10000000;
    int min_index = start;
    for (int i=start; i<(end+1); i++){
        if (arr[i] < min){
            min = arr[i];
            min_index = i;
        }
    }
    return min_index;
}

int row_of_array_min(double *arr, int width, int row, int row_start, int row_end){
    int abs_start = (row * width) + row_start;
    int abs_end = (row * width) + row_end;
    int abs_min_index = array_min(arr, abs_start, abs_end);
    int row_min_index = abs_min_index % width;
    return row_min_index;
}

/*****************************************************
 *****************************************************/


void calc_energy(struct rgb_img *im, struct rgb_img **grad)
{
    double delta_sqrd_x, delta_sqrd_y, col_x, col_y;
    uint8_t energy;
    create_img(grad, im->height, im->width);
    for (int y=0; y<(im->height); y++){
        for (int x=0; x<(im->width); x++){
            delta_sqrd_x = 0;
            delta_sqrd_y = 0;
            for (int col=0; col<3; col++){
                col_x = get_pixel(im, y, (x+1)%(im->width), col) - get_pixel(im, y, (x-1+(im->width))%(im->width), col);
                col_y = get_pixel(im, (y+1)%(im->height), x, col) - get_pixel(im, (y-1+(im->height))%(im->height), x, col);
                delta_sqrd_x += pow(col_x, 2);
                delta_sqrd_y += pow(col_y, 2);
            }
            energy = (uint8_t)((sqrt(delta_sqrd_x + delta_sqrd_y)) / 10);
            set_pixel(*grad, y, x, energy, energy, energy);
        }
    }
    return;
}


void dynamic_seam(struct rgb_img *grad, double **best_arr)
{
    int width = grad->width; int height = grad->height;
    int len_best_arr = width * height;
    int min_prev_cost;
    *best_arr = malloc(len_best_arr * sizeof(double));

    /* initialize first row of cost */
    for (int i=0; i<(grad->width); i++){
        (*best_arr)[i] = get_pixel(grad, 0, i, 0);
    }

    for (int i=1; i<height; i++){
        for (int j=0; j<width; j++){
            min_prev_cost = 1000000000;
            for (int x=-1; x<2; x++){
                if ( (j+x)<0 || (j+x)>(width-1) ){
                    continue;
                }
                if ( (*best_arr)[(i-1)*width+j+x] < min_prev_cost ){
                    min_prev_cost = (*best_arr)[(i-1)*width+j+x];
                }
            }
            (*best_arr)[i*width+j] = get_pixel(grad, i, j, 0) + min_prev_cost;
        }
    }
    return;
}


void recover_path(double *best, int height, int width, int **path)
{
    int last_row_index, prev_row_index, cur_row_index, start_index, end_index;

    *path = malloc(height * sizeof(int));

    /* find minimum in last row first, then work backwards */
    last_row_index = row_of_array_min(best, width, height-1, 0, width-1);
    (*path)[height-1] = last_row_index;
    prev_row_index = last_row_index;

    /* starting with second last row, loop to first*/
    for (int row=(height-2); row>-1; row--){
        start_index = prev_row_index - 1;
        end_index = prev_row_index + 1;
        if (prev_row_index == 0){
            start_index = 0;
        } else if (prev_row_index == (width-1)){
            end_index = width - 1;
        }
        cur_row_index = row_of_array_min(best, width, row, start_index, end_index);
        (*path)[row] = cur_row_index;
        prev_row_index = cur_row_index;
    }
    return;
}


void remove_seam(struct rgb_img *src, struct rgb_img **dest, int *path)
{
    int pixel_to_copy, r, g, b;
    create_img(dest, src->height, (src->width)-1);

    /* loop through pixels of dest, copy corresponding pixel from src */
    for (int y=0; y<((*dest)->height); y++){
        for (int x=0; x<((*dest)->width); x++){
            pixel_to_copy = x;
            /* if pixel index is >= pixel to be removed, get the next pixel from the source */
            if (x >= path[y]){ 
                pixel_to_copy = x + 1;
            }
            r = get_pixel(src, y, pixel_to_copy, 0);
            g = get_pixel(src, y, pixel_to_copy, 1);
            b = get_pixel(src, y, pixel_to_copy, 2);
            set_pixel(*dest, y, x, r, g, b);
        }
    }
    return;
}


// int main(void)
// {
//     /***************************************
//      * TESTING ON 6X5 IMAGE
//      ***************************************/
//     if (DEBUG){
//     char *infile = "6x5.bin";
//     struct rgb_img *im;
//     read_in_img(&im, infile);
//     printf("ORIGINAL IMAGE:\n");
//     print_image(im);

//     struct rgb_img *grad;
//     calc_energy(im, &grad);
//     printf("ENERGY GRADIENT:\n");
//     print_grad(grad);
//     printf("\n\n");

//     double *best_arr;
//     dynamic_seam(grad, &best_arr);
//     printf("COST ARRAY:\n");
//     print_double_array(best_arr, grad->height, grad->width);
//     printf("\n\n");

//     int *path;
//     recover_path(best_arr, grad->height, grad->width, &path);
//     printf("PATH:\n");
//     print_int_array(path, 1, grad->height);
//     printf("\n\n");

//     struct rgb_img *dest;
//     remove_seam(im, &dest, path);
//     printf("REMOVED SEAM IMAGE:\n");
//     print_image(dest);
//     printf("\n\n");
//     }

//     /******************************************
//      *  VISUALIZING SEAM CARVING 
//      ******************************************/
//     if (VISUALIZE){
//     struct rgb_img *im;
//     struct rgb_img *cur_im;
//     struct rgb_img *grad;
//     double *best;
//     int *path;

//     read_in_img(&im, "HJoceanSmall.bin");
    
//     for(int i = 0; i < 5; i++){
//         printf("i = %d\n", i);
//         calc_energy(im,  &grad);
//         dynamic_seam(grad, &best);
//         recover_path(best, grad->height, grad->width, &path);
//         remove_seam(im, &cur_im, path);

//         char filename[200];
//         sprintf(filename, "img%d.bin", i);
//         write_img(cur_im, filename);


//         destroy_image(im);
//         destroy_image(grad);
//         free(best);
//         free(path);
//         im = cur_im;
//     }
//     destroy_image(im);
//     }

//     return 0;
// }