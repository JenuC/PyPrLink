Starting with version 4.2.3.6 of the “Image-Block Ripping Utility” program, a number of command line arguments/options have been added.  This feature addition allows for external software control of the “Image-Block Ripping Utility” program.

| Short Form | Long Form                   | Argument(s)           |
|------------|-----------------------------|------------------------|
| -dr        | -DeleteRaw                  | None                   |
| -kr        | -KeepRaw                    | None                   |
| -cfl       | -ClearFileList              | None                   |
| -arf       | -AddRawFile                 | Full File Path and Name|
| -arfwsf    | -AddRawFileWithSubFolders   | Full File Path         |
| -rtid      | -RipToInputDirectory        | None                   |
| -dnrtid    | -DoNotRipToInputDirectory   | None                   |
| -cnv       | -Convert                    | None                   |
| -sod       | -SetOutputDirectory         | Full File Path         |
| -isf       | -IncludeSubFolders          | None                   |
| -dnisf     | -DoNotIncludeSubFolders     | None                   |

Command Descriptions

-dr/-DeleteRaw:  This option will cause the checkbox labeled “Delete original data after creating images?” to be checked.  Example: “Image-Block Ripping Utility” -dr

-kr/-KeepRaw:  This option will cause the checkbox labeled “Delete original data after creating images?” to be un-checked.  Example: “Image-Block Ripping Utility” -kr

-cfl/-ClearFileList:  This option will clear the current “Block File List(s)”.  Example: “Image-Block Ripping Utility” -cfl

-arf/-AddRawFile:  This option will add the specified file to the “Block File List(s)”.  If the specified file does not exist, an error message will be displayed.  Example: “Image-Block Ripping Utility” –arf “C:\Data\Exp1\Cycle00001_Filelist.txt”

-arfwsf/-AddRawFileWithSubFolders:  For this option to work, the “Include Sub-folders” checkbox must be checked (this can be done via the “–isf” command).  This option will start at the specified directory and search it and all sub-directories for any directories that contain valid file(s) for conversion from the Prairie RAW format to TIFF images.  A “valid” file is one that has a name that ends with “Filelist.txt”.  If the specified directory does not exist, an error message will be displayed.  Example: “Image-Block Ripping Utility” –arfwsf “C:\Data\Exp1”

-rtid/-RipToInputDirectory:  This option will cause the checkbox labeled “Rip image(s) to input directory” to be checked.  Example: “Image-Block Ripping Utility” -rtid

-dnrtid/-DoNotRipToInputDirectory:  This option will cause the checkbox labeled “Rip image(s) to input directory” to be un-checked.  Example: “Image-Block Ripping Utility” –dnrtid

-cnv/-Convert:  This option will cause the program to start the conversion process on the list of files shown in the “Block File List(s)”.  Example: “Image-Block Ripping Utility” –cnv

-sod/-SetOutputDirectory:  This option allows the operator to specify a directory to save the TIFF images into other than the directory where the RAW files are located.  For this option to work, the “Rip image(s) to input directory” checkbox must be un-checked (this can be done via the  -dnrtid command).

-isf/-IncludeSubFolders:  This option will cause the checkbox labeled “Include Sub-folders” to be checked.  Example: “Image-Block Ripping Utility” –isf

-dnisf/-DoNotIncludeSubFolders:  This option will cause the checkbox labeled “Include Sub-folders” to be un-checked.  Example: “Image-Block Ripping Utility” –dnisf

General Notes

For commands that take arguments (e.g. –arf) it is highly recommended that the arguments be enclosed in double quotes (“”).  This will allow the software to correctly handle file names and directory names with spaces in them.

If you wish to specify a directory other than the directory where the raw data files are located as the destination directory for the TIFF images, that directory must be specified before adding the “Filelist.txt” file via the –arf option.  The preferred command ordering would be something like follows:

“Image-Block Ripping Utility” –dnrtid –sod “C:\experiment 1A\analysis” –arf “C:\experiment1A” –cnv

If the operator does not desire to delete the raw data files after the conversion is complete, the –kr flag should be added in the above before the “cnv” command:

“Image-Block Ripping Utility” –dnrtid –sod “C:\experiment 1A\analysis” –arf “C:\experiment1A” -kr –cnv
