
				##############                        TASK 1               #################

# Create a folder called ​ Lab7\step1​ with the following files: ​ bar.txt​ , ​ dir.txt​ ,
# dirList.txt​ , ​ foobar.txt​ , ​ foo2.txt​ , and ​ foo.txt​ .


#######################         USE FUNCTION         ###########
FUNCTION makeFiles($folderName, $fileNames){

New-Item -Path ".\$folderName" -ItemType directory -Force
Foreach ($x in $fileNames)
{
New-Item -Path ".\$folderName\$x" -ItemType File -Force
}
	return 
}

# Folder name
$folderName = "Lab7\step1"

# Make n files
$filenames = @('bar.txt', 'dir.txt', 'dirList.txt', 'foobar.txt', 'foo2.txt', 'foo.txt')

makeFiles $folderName $fileNames



# ######################         By FOR LOOP            #################

# Create a folder named $folderName
$folderName = "NewFolder"
New-Item -Path '.\$folderName' -ItemType directory -Force


# Create a folder named NewFolder
$folderName = "NewFolder"
New-Item -Path ".\$folderName" -ItemType directory -Force


# Create a file
$fileName = "newFile.txt"
New-Item -Path $fileName -ItemType File -Force

# Make n files
$filenames = @('bar.txt', 'dir.txt', 'dirList.txt', 'foobar.txt', 'foo2.txt', 'foo.txt')

# Print array
$fileNames



# Print array with loop
Foreach ($x in $fileNames)
{
$x
}




New-Item -Path ".\$folderName" -ItemType directory -Force

Foreach ($x in $fileNames)
{
$x
New-Item -Path ".\$folderName\$x" -ItemType File -Force
}




# Show all childs

Get-ChildItem -Path .\f*.txt -Recurse -Force

# Copy a folder and all its contents

$path = ".\Lab7\step1"
$des = "."
Copy-Item -Path $path -Destination $des -Recurse