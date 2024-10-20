import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def display_images_from_folder(base_folder, folder_name, ncols=3):
    resolution_folder = os.path.join(base_folder, folder_name)

    if not os.path.isdir(resolution_folder):
        print(f"Folder '{folder_name}' not found in '{base_folder}'.")
        return

    images = [os.path.join(resolution_folder, img) for img in os.listdir(resolution_folder) 
              if img.endswith(('.png', '.jpg', '.jpeg'))]
    
    nrows = (len(images) + ncols - 1) // ncols

    plt.figure(figsize=(15, 5 * nrows))
    plt.suptitle(folder_name)

    for i, img_path in enumerate(images):
        img = mpimg.imread(img_path)
        plt.subplot(nrows, ncols, i + 1)
        plt.imshow(img)
        plt.axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def main() -> None:
    display_images_from_folder('src/responsiveWiz/uploads/ved.rocks', '3840x2160')


if __name__ == '__main__':
    main()